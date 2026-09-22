import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from textwrap import fill
from matplotlib.patches import Rectangle
from matplotlib.colors import TwoSlopeNorm
from aux_func import color_palette, code_to_state


def barplot_best_models(
    df,
    challenge=None,
    model_col="best_model",
    figsize=(10, 6),
    xlabel="Number of states",
    ylabel="Model",
    title="Number of states where the model ranked best",
    save_path="figures",
    dpi=300,
):
    """
    Plot the number of states where each model ranked first.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the best model for each state.
    challenge : str, optional
        Challenge name used in the output filename.
    model_col : str, default="best_model"
        Column containing the model names.
    figsize : tuple, default=(10, 6)
        Figure size.
    xlabel : str
        X-axis label.
    ylabel : str
        Y-axis label.
    title : str
        Plot title.
    save_path : str
        Directory where the figure will be saved.
    dpi : int
        Figure resolution.
    """

    counts = df[model_col].value_counts()

    fig, ax = plt.subplots(figsize=figsize)

    counts.plot(
        kind="barh",
        ax=ax,
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    ax.invert_yaxis()
    ax.grid(axis="x")

    plt.tight_layout()

    if challenge is not None:
        filename = f"{save_path}/count_best_models_{challenge}.png"
    else:
        filename = f"{save_path}/count_best_models.png"

    plt.savefig(filename, dpi=dpi, bbox_inches="tight")
    plt.show()
    plt.close(fig)

def plot_rankplot(
    df,
    colors,
    x_col,
    x_label,
    title,
    region=41,
    validation_ticks=[1, 2, 3, 4],
    figsize=(18, 7),
    x_ticks=None,
    x_lim=None,
    ncols_legend=6,
    bbox_to_anchor=(0.5, -0.25), 
    challenge = 'dengue',
    region_col = 'adm_1',
    region_name = None
):
    
    df = df.loc[df[region_col] == region]

    models = df.model.unique()

    _, ax = plt.subplots(figsize=figsize)

    for i, model in enumerate(models):
        df_to_plot = df.loc[df.model == model]

        ax.plot(
            df_to_plot[x_col],
            df_to_plot["validation"],
            color=colors[model],
            label=model,
            marker=".",
            markersize=18,
            linewidth = 2
        )

    if x_ticks is not None:
        ax.set_xticks(x_ticks)

    ax.set_yticks(validation_ticks)

    ax.set_xlabel(x_label)
    ax.set_ylabel("Validation")

    if x_lim is not None:
        ax.set_xlim(x_lim)

    ax.grid(axis="y")

    ax.legend(
        bbox_to_anchor=bbox_to_anchor,
        ncols=ncols_legend,
    )

    if region_name is not None:
        title = f"{title} in state: {region_name}"

    ax.set_title(title)

    plt.savefig(f'figures/rankplot_{region}_{x_col}_{challenge}.png', dpi = 400, bbox_inches = 'tight')
    
    plt.show()


def plot_zoom_state(
    state,
    df_dengue,
    df_preds,
    df_summary,
    code_to_state,
    color_palette,
    zoom_start,
    zoom_end,
    model_base="PROCC",
    figsize=(10, 5),
    savepath=None,
    loc_legend = 'upper left',
    disease = 'dengue',
    ylim = None 
):
    """
    Plot dengue observations and model predictions for one state,
    with an inset showing the complete historical series.
    """

    # -------------------------------------------------------------------------
    # Data
    # -------------------------------------------------------------------------

    df_dengue_st = df_dengue.query("adm_1 == @state").copy()
    df_preds_st = df_preds.query("adm_1 == @state").copy()

    df_zoom = df_dengue_st.query(
        "@zoom_start <= date <= @zoom_end"
    )

    best_models = (
        df_summary.loc[
            (df_summary.adm_1 == code_to_state[state])
            & (df_summary.geometric_mean_ratio < 1),
            "model",
        ]
        .tolist()
    )

    # -------------------------------------------------------------------------
    # Figure
    # -------------------------------------------------------------------------

    fig, ax = plt.subplots(figsize=figsize)

    axins = inset_axes(
        ax,
        width="32%",
        height="40%",
        loc="upper right",
        borderpad=1,
    )

    # -------------------------------------------------------------------------
    # Observations
    # -------------------------------------------------------------------------

    for axis, data in zip([ax, axins], [df_zoom, df_dengue_st]):

        axis.plot(
            data.date,
            data.casos,
            color="black",
            marker=".",
            linewidth=1.5,
            zorder=1,
            label="Observed" if axis is ax else None,
        )

    # -------------------------------------------------------------------------
    # Predictions
    # -------------------------------------------------------------------------

    for model, df_model in df_preds_st.groupby("model"):

        df_model = df_model.sort_values("date")

        if model == model_base:

            color = color_palette[model]
            alpha = 1
            lw = 2.5
            label = "Baseline"

        elif model in best_models:

            color = color_palette[model]
            alpha = 1
            lw = 2
            label = model

        else:

            color = "0.7"
            alpha = 0.3
            lw = 1
            label = None

        for axis in [ax, axins]:

            axis.plot(
                df_model.date,
                df_model.pred,
                color=color,
                alpha=alpha,
                linewidth=lw,
                label=label,
                zorder=5,
            )

    # -------------------------------------------------------------------------
    # Rectangle indicating zoom
    # -------------------------------------------------------------------------

    rect = Rectangle(
        (mdates.date2num(zoom_start), 0),
        mdates.date2num(zoom_end) - mdates.date2num(zoom_start),
        df_dengue_st.casos.max() * 1.05,
        facecolor="none",
        edgecolor="red",
        linewidth=1.2,
    )

    axins.add_patch(rect)

    # -------------------------------------------------------------------------
    # Formatting
    # -------------------------------------------------------------------------

    ax.set_xlim(zoom_start, zoom_end)
    ax.set_ylabel("Weekly cases")

    ax.set_title(f"{disease.capitalize()} cases and predictions — {code_to_state[state]}")

    ax.grid(alpha=0.3)

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    axins.set_xlim(
        df_dengue_st.date.min(),
        df_dengue_st.date.max() + pd.Timedelta(weeks=20),
    )

    axins.set_ylim(
        0,
        df_dengue_st.casos.max() * 1.05,
    )

    axins.tick_params(axis="x", rotation=45, labelsize=7)
    axins.tick_params(axis="y", labelsize=7)

    handles, labels = ax.get_legend_handles_labels()

    n = len(labels)

    fontsize = 10          # tamanho padrão
    x_outside = 4         # acima disso coloca fora
    x_two_cols = 16       # acima disso usa duas colunas

    kwargs = {
        "fontsize": fontsize,
        "frameon": False,
    }

    if n > x_outside:
        kwargs.update({
            "loc": "center left",
            "bbox_to_anchor": (1.02, 0.5),  # fora do gráfico
        })
    else:
        kwargs.update({
            "loc": loc_legend,
        })

    if n > x_two_cols:
        kwargs["ncol"] = 2

    ax.legend(handles, labels, **kwargs)

    if ylim is not None: 
        ax.set_ylim([0, ylim])

    if savepath is not None:
        plt.savefig(savepath, dpi=300, bbox_inches="tight")

    return fig, ax


def plot_zoom_city(
    city,
    df_dengue,
    df_preds,
    df_summary,
    city_name,
    color_palette,
    zoom_start,
    zoom_end,
    model_base="PROCC",
    figsize=(10, 5),
    savepath=None,
    loc_legend = 'upper left',
    disease = 'dengue'
):
    """
    Plot dengue observations and model predictions for one state,
    with an inset showing the complete historical series.
    """

    # -------------------------------------------------------------------------
    # Data
    # -------------------------------------------------------------------------

    df_dengue_st = df_dengue.query("adm_2 == @city").copy()
    df_preds_st = df_preds.query("adm_2 == @city").copy()

    df_zoom = df_dengue_st.query(
        "@zoom_start <= date <= @zoom_end"
    )

    best_models = (
        df_summary.loc[
            (df_summary.adm_2 == city)
            & (df_summary.geometric_mean_ratio < 1),
            "model",
        ]
        .tolist()
    )

    # -------------------------------------------------------------------------
    # Figure
    # -------------------------------------------------------------------------

    fig, ax = plt.subplots(figsize=figsize)

    axins = inset_axes(
        ax,
        width="32%",
        height="40%",
        loc="upper right",
        borderpad=1,
    )

    # -------------------------------------------------------------------------
    # Observations
    # -------------------------------------------------------------------------

    for axis, data in zip([ax, axins], [df_zoom, df_dengue_st]):

        axis.plot(
            data.date,
            data.casos,
            color="black",
            marker=".",
            linewidth=1.5,
            zorder=1,
            label="Observed" if axis is ax else None,
        )

    # -------------------------------------------------------------------------
    # Predictions
    # -------------------------------------------------------------------------

    for model, df_model in df_preds_st.groupby("model"):

        df_model = df_model.sort_values("date")

        if model == model_base:

            color = color_palette[model]
            alpha = 1
            lw = 2
            label = "Baseline"

        elif model in best_models:

            color = color_palette[model]
            alpha = 1
            lw = 2
            label = model

        else:

            color = "0.7"
            alpha = 0.3
            lw = 1
            label = None

        for axis in [ax, axins]:

            axis.plot(
                df_model.date,
                df_model.pred,
                color=color,
                alpha=alpha,
                linewidth=lw,
                label=label,
                zorder=5,
            )

    # -------------------------------------------------------------------------
    # Rectangle indicating zoom
    # -------------------------------------------------------------------------

    rect = Rectangle(
        (mdates.date2num(zoom_start), 0),
        mdates.date2num(zoom_end) - mdates.date2num(zoom_start),
        df_dengue_st.casos.max() * 1.05,
        facecolor="none",
        edgecolor="red",
        linewidth=1.2,
    )

    axins.add_patch(rect)

    # -------------------------------------------------------------------------
    # Formatting
    # -------------------------------------------------------------------------

    ax.set_xlim(zoom_start, zoom_end)
    ax.set_ylabel("Weekly cases")

    ax.set_title(f"{disease.capitalize()} cases and predictions — {city_name}")

    ax.grid(alpha=0.3)

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    axins.set_xlim(
        df_dengue_st.date.min(),
        df_dengue_st.date.max() + pd.Timedelta(weeks=20),
    )

    axins.set_ylim(
        0,
        df_dengue_st.casos.max() * 1.05,
    )

    axins.tick_params(axis="x", rotation=45, labelsize=7)
    axins.tick_params(axis="y", labelsize=7)

    handles, labels = ax.get_legend_handles_labels()

    n = len(labels)

    fontsize = 10          # tamanho padrão
    x_outside = 4         # acima disso coloca fora
    x_two_cols = 16       # acima disso usa duas colunas

    kwargs = {
        "fontsize": fontsize,
        "frameon": False,
    }

    if n > x_outside:
        kwargs.update({
            "loc": "center left",
            "bbox_to_anchor": (1.02, 0.5),  # fora do gráfico
        })
    else:
        kwargs.update({
            "loc": loc_legend,
        })

    if n > x_two_cols:
        kwargs["ncol"] = 2

    ax.legend(handles, labels, **kwargs)

    if savepath is not None:
        plt.savefig(savepath, dpi=300, bbox_inches="tight")

    return fig, ax



def style_cells(val, 
                cell_colors = color_palette):
    """background das células de dados (mantém texto em negrito)."""
    bg = cell_colors.get(val, "white")
    return f"background-color: {bg}; font-weight: bold; text-align: center; color: black;"

def style_medal(val, medal_colors = {
    "GOLD":   "#DAA520",   # dourado
    "SILVER": "#B0B0B0",   # prata
    "BRONZE": "#A97142"    # bronze
}):
    """aplica cor apenas ao texto da coluna MEDAL."""
    c = medal_colors.get(val, "black")
    return f"color: {c}; font-weight: bold; text-align: left;"

def plot_medal_board(ranked_models, index = ["GOLD", "SILVER", "BRONZE"]): 

    data = ranked_models

    df = pd.DataFrame(data.values, index=index, columns = data.columns)

    df.index.name = "MEDAL"

    df_reset = df.reset_index()   # agora há uma coluna "MEDAL" + as colunas originais

    styler = df_reset.style

    # estiliza todas as células de dados (todas colunas exceto 'MEDAL'):
    data_cols = [c for c in df_reset.columns if c != "MEDAL"]
    styler = styler.map(style_cells, subset=pd.IndexSlice[:, data_cols])

    # estiliza apenas a coluna MEDAL (texto colorido)
    styler = styler.map(style_medal, subset=pd.IndexSlice[:, ["MEDAL"]])

    # estilos gerais da tabela (bordas, fonte, cabeçalho)
    styler = styler.set_table_styles([
        {"selector": "th", "props": [("font-weight", "bold"), ("text-align", "center"), ("border", "1px solid black")]},
        {"selector": "td", "props": [("border", "1px solid black"), ("padding", "6px")]},
        {"selector": "table", "props": [("border-collapse", "collapse"), ("font-family", "Arial"), ("font-size", "13px")]}
    ])

    styler = styler.hide(axis="index")  # hides the index completely

    return styler


def plot_geometric_ratio_heatmap(
    df_summary,
    regions,
    label,
    figsize=(25, 5),
    challenge = None,
    col = 'adm_1',
    ylabel = 'State',
    rotation = 60
):
    """
    Plot a heatmap of the geometric mean ratio by state and model.

    Parameters
    ----------
    df_summary : pd.DataFrame
        Summary dataframe containing 'adm_1', 'model' and
        'geometric_mean_ratio'.
    code_to_state : dict
        Dictionary mapping state codes to state abbreviations.
    states : list[str]
        States to include in the plot, in the desired order.
    label : str
        Output filename (without extension).
    figsize : tuple, optional
        Figure size.
    """

    df = df_summary.copy()

    df_pivot = (
        df.loc[df[col] != 'ES']
        .pivot(index=col, columns="model", values="geometric_mean_ratio")
        .loc[regions]
    )

    try: 

        norm = TwoSlopeNorm(
            vmin=df_pivot.values.min(),
            vcenter=1,
            vmax=min(2, df_pivot.values.max()),
        )

    except: 
        norm = TwoSlopeNorm(
            vmin=0.5,
            vcenter=1,
            vmax=min(2, df_pivot.values.max()),
        )


    fig, ax = plt.subplots(figsize=figsize)

    im = ax.imshow(
        df_pivot.values,
        cmap="RdYlGn_r",
        norm=norm,
        aspect="auto",
    )

    # Tick labels
    ax.set_xticks(np.arange(df_pivot.shape[1]))
    ax.set_yticks(np.arange(df_pivot.shape[0]))

    ax.set_xticklabels(
        [
            fill(col.replace("_", " "), width=18).replace(" ", "\n")
            for col in df_pivot.columns
        ]
    )
    ax.set_yticklabels(df_pivot.index)

    # Cell values
    for i in range(df_pivot.shape[0]):
        for j in range(df_pivot.shape[1]):
            ax.text(
                j,
                i,
                f"{df_pivot.iloc[i, j]:.2f}",
                ha="center",
                va="center",
                color="black",
            )

    #plt.colorbar(im, ax=ax, label="E_model / E_baseline")

    ax.set_xlabel("Model")
    ax.set_ylabel(ylabel)
    ax.set_title(
        "Geometric mean of the ratio (E_model/E_baseline) across the four validation sets"
    )

    plt.setp(ax.get_xticklabels(), rotation=rotation, ha="right")

    fig.tight_layout()

    fig.savefig(f"figures/heatmap_{label}_{challenge}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_matrix(
    df_summary,
    regions,
    figsize=(25, 5),
    challenge=None,
    transpose=False,
    col = 'adm_1',
    xlabel = 'State',
    rotation = 60, 
    region_sep = True, 
):
    """
    Plot a categorical heatmap of the geometric mean ratio by state and model.

    Parameters
    ----------
    transpose : bool, default=False
        False -> rows = states, columns = models
        True  -> rows = models, columns = states
    """

    df = df_summary.copy()

    # ------------------------------------------------------------------
    # Pivot
    # ------------------------------------------------------------------

    df_pivot = (
        df.loc[df[col] != 32]
        .pivot(index=col, columns="model", values="geometric_mean_ratio")
        .loc[regions]
    )

    # ------------------------------------------------------------------
    # Model ordering
    # ------------------------------------------------------------------

    ranking = pd.DataFrame(
        {
            "green": (df_pivot < 0.95).sum(axis=0),
            "red": (df_pivot > 1.05).sum(axis=0),
            "mean_ratio": df_pivot.mean(axis=0),
        }
    )

    order = (
        ranking.sort_values(
            by=["green", "red", "mean_ratio"],
            ascending=[False, True, True],
        )
        .index
    )

    df_pivot = df_pivot[order]

    # ------------------------------------------------------------------
    # Transpose (optional)
    # ------------------------------------------------------------------

    if transpose:
        df_plot = df_pivot.T
    else:
        df_plot = df_pivot

    # ------------------------------------------------------------------
    # Categorize
    # ------------------------------------------------------------------

    df_colors = np.where(
        df_plot.values < 0.95,
        -1,
        np.where(df_plot.values > 1.05, 1, 0),
    )

    cmap = ListedColormap(["#66bd63", "white", "#d73027"])

    fig, ax = plt.subplots(figsize=figsize)

    ax.imshow(
        df_colors,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        aspect="auto",
    )

    # ------------------------------------------------------------------
    # Axis ticks
    # ------------------------------------------------------------------

    ax.set_xticks(np.arange(df_plot.shape[1]))
    ax.set_yticks(np.arange(df_plot.shape[0]))

    if transpose:

        ax.set_xticklabels(df_plot.columns)

        ax.set_yticklabels([
            fill(model.replace("_", " "), width=18).replace(" ", "\n")
            for model in df_plot.index
        ])

        ax.set_xlabel(xlabel)
        ax.set_ylabel("Model")

        plt.setp(
            ax.get_xticklabels(),
            rotation=0,
            ha="center",
        )

    else:

        ax.set_xticklabels([
            fill(model.replace("_", " "), width=18).replace(" ", "\n")
            for model in df_plot.columns
        ])

        ax.set_yticklabels(df_plot.index)

        ax.set_xlabel("Model")
        ax.set_ylabel(xlabel)

        plt.setp(
            ax.get_xticklabels(),
            rotation=rotation,
            ha="right",
        )

    # ------------------------------------------------------------------
    # Title
    # ------------------------------------------------------------------

    ax.set_title(
        "Geometric mean ratio (Model / Baseline)\n"
        "Green: <0.95   White: 0.95–1.05   Red: >1.05"
    )

    # ------------------------------------------------------------------
    # Region separators
    # ------------------------------------------------------------------
    if region_sep: 
        region_breaks = [3, 6, 10, 19]

        if transpose:

            for x in region_breaks:
                ax.axvline(
                    x - 0.5,
                    color="black",
                    linewidth=2.5,
                )

        else:

            for y in region_breaks:
                ax.axhline(
                    y - 0.5,
                    color="black",
                    linewidth=2.5,
                )

    # ------------------------------------------------------------------
    # Grid
    # ------------------------------------------------------------------

    ax.set_xticks(
        np.arange(-0.5, df_plot.shape[1], 1),
        minor=True,
    )

    ax.set_yticks(
        np.arange(-0.5, df_plot.shape[0], 1),
        minor=True,
    )

    ax.grid(
        which="minor",
        color="gray",
        linestyle="-",
        linewidth=0.5,
    )

    ax.tick_params(
        which="minor",
        bottom=False,
        left=False,
    )

    fig.tight_layout()

    if challenge is not None:

        suffix = "_T" if transpose else ""

        fig.savefig(
            f"figures/matrix_BR_{challenge}{suffix}.png",
            dpi=300,
            bbox_inches="tight",
        )

    return fig, ax, ranking.loc[order]

def plot_violin(df_rank, region = None, challenge = None): 

    if region is not None: 
        df_rank = df_rank.loc[df_rank.region == region]
    Q1 = df_rank["wis_ratio"].quantile(0.25)
    Q3 = df_rank["wis_ratio"].quantile(0.75)
    IQR = Q3 - Q1

    df_filtrado = df_rank[
        (df_rank["wis_ratio"] >= Q1 - 1.5 * IQR) &
        (df_rank["wis_ratio"] <= Q3 + 1.5 * IQR)
    ]

    order = df_filtrado["model"].unique()

    # Mediana de cada modelo
    medianas = df_filtrado.groupby("model")["wis_ratio"].median()

    # Cria uma cor para cada modelo
    palette = {
        model: "tab:green" if medianas[model] < 1 else "tab:blue"
        for model in order
    }



    fig, ax = plt.subplots(figsize=(15, 5))

    sns.violinplot(
        data=df_filtrado,
        x="model",
        y="wis_ratio",
        inner=None,
        palette=palette,
        ax=ax,
    )

    sns.boxplot(
        data=df_filtrado,
        x="model",
        y="wis_ratio",
        width=0.15,
        showcaps=True,
        showfliers=False,
        boxprops={"facecolor": "none"},
        whiskerprops={"color": "black"},
        medianprops={"color": "white", "linewidth": 2},
        capprops={"color": "black"},
        ax=ax,
    )

    # Obtém os rótulos atuais
    labels = [
        fill(label.get_text().replace("_", " "), width=18).replace(" ", "\n")
        for label in ax.get_xticklabels()
    ]

    # Define posições e rótulos
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(labels, rotation=90, fontdict={'size': 12},  ha="center",
        va="top")

    ax.axhline(1, color = 'red', linestyle = '--')
    ax.set_ylabel('WIS_model/WIS_baseline')

    if region is not None: 
        ax.set_title(f'Ratio between WIS model and baseline in {region}')
    else: 
        ax.set_title('Ratio between WIS model and baseline')

    plt.tight_layout()

    if region is not None: 
        plt.savefig(f'figures/violin_{region}_{challenge}.png', dpi = 400, bbox_inches = 'tight')
    else: 
        plt.savefig(f'figures/violin_{challenge}.png', dpi = 400, bbox_inches = 'tight')
    
    plt.show()

    return fig, ax 


def plot_swarmplot(df_rank, region = None): 

    if region is not None: 
        df_rank = df_rank.loc[df_rank.region == region]
    Q1 = df_rank["wis_ratio"].quantile(0.25)
    Q3 = df_rank["wis_ratio"].quantile(0.75)
    IQR = Q3 - Q1

    df_filtrado = df_rank[
        (df_rank["wis_ratio"] >= Q1 - 1.5 * IQR) &
        (df_rank["wis_ratio"] <= Q3 + 1.5 * IQR)
    ]

    order = df_filtrado["model"].unique()

    # Mediana de cada modelo
    medianas = df_filtrado.groupby("model")["wis_ratio"].median()

    # Cria uma cor para cada modelo
    palette = {
        model: "tab:green" if medianas[model] < 1 else "tab:blue"
        for model in order
    }



    fig, ax = plt.subplots(figsize=(15, 5))

    sns.stripplot(
        data=df_filtrado,
        x="model",
        y="wis_ratio",
        hue="validation",
        palette="tab10",      # ou "viridis", "tab10", etc.
        dodge=False,         # True separa horizontalmente por validation
        size=3.5,
        alpha=0.8,
        ax=ax
    )

    sns.boxplot(
        data=df_filtrado,
        x="model",
        y="wis_ratio",
        width=0.15,
        showcaps=True,
        showfliers=False,
        boxprops={"facecolor": "none"},
        whiskerprops={"color": "black"},
        medianprops={"color": "white", "linewidth": 2},
        capprops={"color": "black"},
        ax=ax,
        zorder = 5
    )

    # Obtém os rótulos atuais
    labels = [
        fill(label.get_text().replace("_", " "), width=18).replace(" ", "\n")
        for label in ax.get_xticklabels()
    ]

    # Define posições e rótulos
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(labels, rotation=90, fontdict={'size': 12},  ha="center",
        va="top")

    ax.axhline(1, color = 'red', linestyle = '--')
    ax.set_ylabel('WIS_model/WIS_baseline')

    if region is not None: 
        ax.set_title(f'Ratio between WIS model and baseline in {region}')
    else: 
        ax.set_title('Ratio between WIS model and baseline')

    ax.legend(loc= (1.01, 0.6))
    #plt.tight_layout()

    #if region is not None: 
    #    plt.savefig(f'figures/ratio_models_{region}.png', dpi = 400, bbox_inches = 'tight')
    #else: 
    #    plt.savefig('figures/ratio_models.png', dpi = 400, bbox_inches = 'tight')
    
    #plt.show()

    return fig, ax 


def plot_parameters(ax, df_true_params, df_pars, region, val, column = 'peak_week', title = '', col_region = 'state'): 

    if column == 'peak_week': 
        label = 'pico_dist_p50'

    elif column == 'total_cases': 
        label = 'season_total_p50'
    
    elif column == 'peak_height': 
        label = 'season_peak_p50'

    elif column == 't_ini':
        label = 't_ini_dist_p50'

    df_true_ = df_true_params.loc[(df_true_params[col_region]== region) & (df_true_params.validation == val)]

    df_pars_ = df_pars.loc[(df_pars[col_region] == region) & (df_pars.validation == val )]

    ax.hist(df_pars_[label])
    ax.axvline(df_true_[column].values[0], color = 'red', linestyle = '--', label= 'Observed')

    ax.set_title(title)


def plot_parameter_histograms(
    df_true_params,
    df_pars,
    region,
    validations=(2, 3, 4),
    parameters=(
        ("peak_week", "Peak week"),
        ("peak_height", "Max cases"),
        ("total_cases", "Total cases"),
        ("t_ini", 'Ini week')
    ),
    figsize=(16, 8),
    label_title = '',
    col_region = 'state'
):
    """
    Plot histograms comparing estimated and true parameters for multiple
    validation sets.

    Parameters
    ----------
    df_true_params : pandas.DataFrame
        DataFrame containing the reference parameters.
    df_pars : pandas.DataFrame
        DataFrame containing the estimated parameters.
    state : int
        State code.
    code_to_state : dict
        Dictionary mapping state codes to state names.
    validations : iterable of int, optional
        Validation IDs to plot.
    parameters : iterable of tuple(str, str), optional
        List of (column_name, title).
    figsize : tuple, optional
        Figure size.
    """

    n_rows = len(validations)
    n_cols = len(parameters)

    fig, ax = plt.subplots(
        n_rows,
        n_cols,
        figsize=figsize,
        sharex="col",
        squeeze=False,
    )

    for i, val in enumerate(validations):
        ax[i, 0].set_ylabel(f"Validation {val}")

        for j, (column, title) in enumerate(parameters):
            plot_parameters(
                ax=ax[i, j],
                df_true_params=df_true_params,
                df_pars=df_pars,
                region=region,
                val=val,
                column=column,
                title=title if i == 0 else "",
                col_region = col_region
            )

    fig.suptitle(f"Histograms of Parameters - {label_title}", y = 0.92)
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    return fig, ax


def plot_par_bar(ax, column, adm_1, validation, df_pars, df_true_params): 

    if column == 'peak_week': 
        label = 'pico_dist_p50'
        title = 'Peak week'

    elif column == 'total_cases': 
        label = 'season_total_p50'
        title = 'Total cases'
        
    elif column == 'peak_height': 
        label = 'season_peak_p50'
        title = 'Max cases'

    elif column == 't_ini':
        label = 't_ini_dist_p50'
        title = 'Start week'


    df_ = df_pars.loc[(df_pars.state == adm_1) & (df_pars.validation == validation)]

    ax.bar(df_.model, df_[label])
    ax.axhline(df_true_params.loc[(df_true_params.state == adm_1) & (df_true_params.validation == validation)][column].values[0],
            color = 'tab:red', linestyle = '--')

    ax.set_ylabel(title)
    plt.tight_layout()

    ax.set_title(f'{title} - state:{code_to_state[adm_1]}, validation:{validation}')


def plot_model_scatter(
    df_ratio,
    rename_models=None,
    baseline_model="PROCC",
    exclude_adm1=None,
    title="Interannual Model Stability in all states (IMDC)",
    xlabel="Mean log(Rv) → negative = better than the baseline",
    ylabel="Standard deviation of log(Rv) → lower = more stable",
    xlim=(-0.3, 1),
    ylim=(0, 1),
    figsize=(12, 7),
    savepath=None,
    color_palette = None
):
    """
    Plot model stability using the mean and standard deviation of log(WIS ratio).

    Parameters
    ----------
    df_ratio : DataFrame
        Must contain columns ['model', 'wis_ratio'] and optionally 'adm_1'.
    rename_models : dict, optional
        Dictionary to rename model names.
    baseline_model : str
        Baseline model to remove from the plot.
    exclude_adm1 : int or list, optional
        adm_1 values to exclude.
    savepath : str, optional
        If provided, saves the figure.
    """

    df = df_ratio.copy()

    # -------------------------------------------------------------------------
    # Filtering
    # -------------------------------------------------------------------------

    if exclude_adm1 is not None:
        if np.isscalar(exclude_adm1):
            exclude_adm1 = [exclude_adm1]
        df = df.loc[~df.adm_1.isin(exclude_adm1)]

    df["log_ratio"] = np.log(df["wis_ratio"])

    df_agg = (
        df.groupby("model")["log_ratio"]
        .agg(mean="mean", std="std")
        .reset_index()
    )

    if rename_models is not None:
        df_agg["model"] = df_agg["model"].replace(rename_models)

    df_agg = df_agg.loc[df_agg.model != baseline_model]

    median_std = df_agg["std"].median()

    mask = (
        (df_agg["mean"] <= 0)
        & (df_agg["std"] <= median_std)
    )

    xmin, xmax = xlim
    ymin, ymax = ylim

    # -------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------

    fig, ax = plt.subplots(figsize=figsize)

    # Quadrants
    quadrants = [
        ((xmin, ymin), 0 - xmin, median_std, "limegreen"),
        ((xmin, median_std), 0 - xmin, ymax - median_std, "lightskyblue"),
        ((0, median_std), xmax, ymax - median_std, "gold"),
        ((0, ymin), xmax, median_std, "tomato"),
    ]

    for (xy, w, h, color) in quadrants:
        ax.add_patch(
            Rectangle(
                xy,
                w,
                h,
                facecolor=color,
                alpha=0.10,
                zorder=0,
            )
        )

    # Other models
    ax.scatter(
        df_agg.loc[~mask, "mean"],
        df_agg.loc[~mask, "std"],
        color="gray",
        alpha=0.5,
        s=40,
        label="Other models",
    )

    
    for _, row in df_agg.loc[mask].iterrows():

        print(row['model'])

        ax.scatter(
            row["mean"],
            row["std"],
            color=color_palette[row['model']],
            s=70,
            edgecolor="black",
            linewidth=0.5,
            label=row["model"],
        )

    # Reference lines
    ax.axvline(0, color="gray", linestyle=":", alpha=0.7)
    ax.axhline(median_std, color="gray", linestyle=":", alpha=0.7)

    # Quadrant labels
    labels = [
        (xlim[0]/2, median_std / 2,
         "Stable", "darkgreen"),

        (xlim[0]/2, (median_std + ymax) / 2,
         "Better than baseline,\nbut inconsistent", "steelblue"),

        (0.5, (median_std + ymax) / 2,
         "Unstable", "darkgoldenrod"),

        (0.5, median_std / 2,
         "Consistently\nworse than baseline", "firebrick"),
    ]

    for x, y, txt, color in labels:
        ax.text(
            x,
            y,
            txt,
            ha="center",
            va="center",
            fontsize=11,
            color=color,
            fontweight="bold",
        )

    # Formatting
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

    ax.set_title(title, fontsize=14, fontweight="bold")

    ax.grid(alpha=0.2)

    ax.legend(
        title="Stable models",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )

    plt.tight_layout()

    if savepath is not None:
        plt.savefig(savepath, dpi=300, bbox_inches="tight")

    return fig, ax, df_agg


