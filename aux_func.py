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

rename_models = {'3rd_imdc_isi_isi-dengue': 'ISI',
                                    '3rd_imdc_purdue_neuralearth': "PURDUE",
                                          '3rd_imdc_fiocruz_mard': "FIOCRUZ_MARD",
                                               '3rd_imdc_bsc_ghr':"BSC",
                                      '3rd_imdc_fgv_pattern-blue':"EMAP_BLUE",
                                '3rd_imdc_lncc_lncc_arp26_dengue':"LNCC_ARP26",
                                        '3rd_imdc_procc_bb_model':"PROCC" ,
                                         '3rd_imdc_unesp_recogna': "UNESP",
                                '3rd_imdc_ifgw_inframind-proteus':"IFGW",
                                                'DS-OKSTATE-2026': "DS-OKSTATE",
                              '3rd_imdc_ceri_returnoftheforecast': "CERI",
                                          '3rd_imdc_nus_nus-cerm':"NUS-CERM",
                             '3rd_imdc_lncc_surge_model26_dengue':"LNCC_SURGE",
                                     '3rd_imdc_pucrio_arbocaster': "PUCRIO",
                                             '3rd_imdc_emap_lstm': "EMAP_LSTM",
                                        '3rd_imdc_emap_xgbsillas': "EMAP_XGB",
 '3rd_imdc_universidad_del_valle_grupo_modelamiento_datos_dengue': "UNI_DEL_VALLE",
                                 '3rd_imdc_lncc_clidengo26dengue': "LNCC_CLIDENGO",
                                      '3rd_imdc_fiocruz_zerolags': "FIOCRUZ_ZEROLAGS",
                                      '3rd_imdc_cornell_bentolab': "CORNELL",
                             '3rd_imdc_emap_epidematicos_prophet': "EMAP_PROPHET",
                                            '3rd_imdc_fgv_sakhal': "EMAP_SAKHAL",
                               '3rd_imdc_rki_rki_zki_ph_lstm_geo': "RKI_LSTM",
                                              '3rd_imdc_afya_ric': "AFYA",
                                        '3rd_imdc_rki_rki_zki_ph': "RKI_PH",
                       '3rd_imdc_emap_epidematicos_sarimax_state': 'EMAP_SARIMAX', 
                       '3rd_imdc_-unifesp-_-4mosqueteiras-': 'UNIFESP',
                                '3rd_imdc_lncc_ARp26_chikungunya': 'LNCC_ARP26',
                                '3rd_imdc_lncc_clidengo26chikungunya':'LNCC_CLIDENGO',
                                '3rd_imdc_lncc_surge_model26_chikungunya':'LNCC_SURGE',
                                '3rd_imdc_emap_epidematicos_sarimax_muni': 'EMAP_SARIMAX',
                                '3rd_imdc_emap_lstm_muni': 'EMAP_LSTM'} 


color_palette = {'UNIFESP': '#d60000',
 'AFYA': '#8c3bff',
 'BSC': '#018700',
 'CERI': '#00acc6',
 'CORNELL': '#97ff00',
 'EMAP_PROPHET': '#ff7ed1',
 'EMAP_SARIMAX': '#6b004f',
 'EMAP_LSTM': '#ffa52f',
 'EMAP_XGB': '#573b00',
 'EMAP_BLUE': '#005659',
 'EMAP_SAKHAL': '#0000dd',
 'FIOCRUZ_MARD': '#00fdcf',
 'FIOCRUZ_ZEROLAGS': '#a17569',
 'IFGW': '#bcb6ff',
 'ISI': '#95b577',
 'LNCC_CLIDENGO': '#bf03b8',
 'LNCC_ARP26': '#645474',
 'LNCC_SURGE': '#790000',
 'NUS-CERM': '#0774d8',
 'PROCC': '#fdf490',
 'PUCRIO': '#004b00',
 'PURDUE': '#8e7900',
 'RKI_PH': '#ff7266',
 'RKI_LSTM': '#edb8b8',
 'UNESP': '#5d7e66',
 'UNI_DEL_VALLE': '#9ae4ff',
 'DS-OKSTATE': '#eb0077'}

## Plots Best models by state: 

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