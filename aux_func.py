import pandas as pd 

code_to_state = {33: 'RJ', 32: 'ES', 41: 'PR', 23: 'CE', 21: 'MA',
 31: 'MG', 42: 'SC', 26: 'PE', 25: 'PB', 24: 'RN', 22: 'PI', 27: 'AL',
 28: 'SE', 35: 'SP', 43: 'RS', 15: 'PA', 16: 'AP', 14: 'RR',  11: 'RO',
 13: 'AM', 12: 'AC', 51: 'MT', 50: 'MS', 52: 'GO', 17: 'TO', 53: 'DF',
 29: 'BA'}

regioes = {
    'North': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Northeast': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Midwest': ['DF', 'GO', 'MT', 'MS'],
    'Southeast': ['ES', 'MG', 'RJ', 'SP'],
    'South': ['PR', 'RS', 'SC']
}

rename_regions = {
    'Norte':'North',
    'Nordeste': 'Northeast' ,
    'Centro-Oeste':'Midwest',
    'Sudeste':'Southeast',
    'Sul':'South'
}

estado_para_regiao = {est: reg for reg, estados in regioes.items() for est in estados}


state_to_code = {value: key for key, value in code_to_state.items()}



geo_dengue = [2931350,2933307,2302503,3119401,
              3549805,3541406,1200401,1200203,
              1716109,4113700,4103701,4104808,
              5201405,5102637,5215231]

geo_chik = [2211001,2931350,3143302,3119401,
            1721000,1716109,4104808,4219507,
            5103403,5102637] 

def get_data(name = 'dengue_state'): 

    df = pd.read_csv(f'data/{name}.csv.gz')

    return df