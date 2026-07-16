import numpy as np 
import scipy.stats as st
import lmfit as lm
from lmfit import Parameters

def estimate_rho(df_grp, eps=1e-12):
    # Pandas usa drop_duplicates e sort_values
    g = df_grp.drop_duplicates(subset=['date'], keep='first').sort_values('date')
    
    mu    = g['mu'].to_numpy()
    sigma = g['sigma'].to_numpy()
    x     = g['casos'].to_numpy().astype(float)
    x[x == 0] = 0.1
 
    with np.errstate(divide='ignore', invalid='ignore'):
        W = (np.log(x) - mu) / sigma
 
    W_t, W_next = W[:-1], W[1:]
 
    n = len(W_t)
    if n < 2 or np.sum(W_t ** 2) < eps:
        return np.nan
        
    rho_ols = np.sum(W_t * W_next) / np.sum(W_t ** 2)
    T = n + 1

    rho = T / (T - 2) * rho_ols

    if rho < -1: 
        return -1 
    elif rho > 1: 
        return 1
    else: 
        return rho 

def sample_path(forecast_marginals, rho, random_state=None):
    horizon = len(forecast_marginals)
    rng = np.random.default_rng(random_state)
    path = np.empty(horizon)
    path[0] = forecast_marginals[0].rvs(random_state=rng)
    for j in range(1, horizon):
        u_prev = np.clip(forecast_marginals[j - 1].cdf(path[j - 1]), 1e-12, 1 - 1e-12)
        z_prev = st.norm.ppf(u_prev)
        z = rng.normal(loc=rho * z_prev, scale=np.sqrt(1 - rho ** 2))
        u = np.clip(st.norm.cdf(z), 1e-12, 1 - 1e-12)
        path[j] = forecast_marginals[j].ppf(u)
    return path

# ----------------------------------------------------------------------
# 5. Per-week marginals for ONE state, ordered by date.
# ----------------------------------------------------------------------
def build_marginals(F_marginals, uf, label='Forecast'):
    # Filtro usando a sintaxe de indexação booleana do Pandas
    df = F_marginals[
        (F_marginals['adm_1'] == uf) & 
        (F_marginals['validation'] == label)
    ]
    
    # Remoção de duplicadas e ordenação
    df = df.drop_duplicates(subset=['date'], keep='first').sort_values('date')
    
    # itertuples() é mais performático que iterrows() no Pandas para essa iteração
    return [
        st.lognorm(s=row.sigma, scale=np.exp(row.mu))
        for row in df.itertuples(index=False)
    ]


@np.vectorize
def richards(L, a, b, t, tj):
    return L - L * (1 + a * np.exp(b * (t - tj))) ** (-1 / a)

def obj_fun_path(params, t, casos_cum):
    p = params.valuesdict()
    L, tp, a, b = p["L1"], p["tp1"], p["a1"], p["b1"]
    err = casos_cum - richards(L, a, b, t, tp)
    return (err**2) / len(t)

# --- Nova função de otimização para um único caminho (array) ---
def otim_single_path(path_array):
    casos_cum = np.cumsum(path_array)
    s = path_array.sum()
    horizon = len(path_array)
    t = np.arange(horizon)
    
    params = Parameters()
    params.add("gamma", min=0.3, max=1.05)
    params.add("L1", min=1.0, max=1.2 * s)
    params.add("tp1", min=5, max=35)
    params.add("b1", min=1e-6, max=1)
    params.add("a1", expr="b1/(gamma + b1)", min=0.001, max=1)
    
    # Executa a otimização por Evolução Diferencial para o caminho atual
    out = lm.minimize(obj_fun_path, params, args=(t, casos_cum), method="nelder")
    p = out.params.valuesdict()
    
    # Extração das métricas de interesse deste caminho:
    semana_pico = p["tp1"]                 # O parâmetro tp1 é o ponto de inflexão (pico diário/semanal)
    r0 = 1 + (p["b1"] / p["gamma"])        # R0 baseado na taxa b1 e no gamma estimado
    
    return r0, semana_pico
