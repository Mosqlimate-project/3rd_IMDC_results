# 3rd Infodengue-Mosqlimate Dengue Challenge (IMDC): 2026 Sprint for dengue fever forecasts for Brazil

The Infodengue-Mosqlimate Dengue Challenge (IMDC) is an initiative led by the Mosqlimate and Infodengue. 

The objective of this 2026 sprint is **to promote training of predictive models and to develop high-quality ensemble forecast models for dengue in Brazil.**

The challenge involves four validation tests and one forecast target. The period of interest spans from the epidemiological week (EW) 41 of one year to EW 40 of the following year, aligning with the typical dengue season in Brazil.

**Validation test 1.** Predict the weekly number of dengue cases by state (UF) in the 2022-2023 season \[EW 41 2022- EW40 2023\], using data covering the period from EW 01 2010 to EW 25 2022;

**Validation test 2.** Predict the weekly number of dengue cases by state (UF) in the 2023-2024 season \[EW 41 2023- EW40 2024\], using data covering the period from EW 01 2010 to EW 25 2023;

**Validation test 3:** Predict the weekly number of dengue cases by state (UF) in the 2024-2025 season \[EW 41 2024- EW40 2025\], using data covering the period from EW 01 2010 to EW 25 2024;

**Validation test 4.** Predict the weekly number of dengue cases in Brazil, and by state (UF), in the 2025-2026 season \[EW 41 2025- EW40 2026\], using data covering the period from EW 01 2010 to EW 25 2025;

**Forecast.** Predict the weekly number of dengue cases in Brazil, and by state (UF), in the 2026-2027 season \[EW 41 2026- EW40 2027\], using data covering the period from EW 01 2010 to EW 25 2026;



This document presents the results for the **Optional Challenge 1 – Dengue (City Level)**: Forecast dengue cases for 15 selected cities. The results for the optional challenges are available in the following files:

* `readme.md` – Dengue (State Level)
* `optional_challenge_2.md` – Chikungunya (State Level)
* `optional_challenge_3.md` – Chikungunya (City Level)

Forecast dengue cases for 15 selected citiesfollowing cities:

* Teixeira de Freitas (BA) - geocode: 2931350
* Vitória da Conquista (BA) - geocode: 2933307
* Brejo Santo (CE) - geocode: 2302503
* Coronel Fabriciano (MG) - geocode: 3119401
* São José do Rio Preto (SP) - geocode: 3549805
* Presidente Prudente (SP) - geocode: 3541406
* Rio Branco (AC) - geocode: 1200401
* Cruzeiro do Sul (AC) - geocode: 1200203
* Paraíso do Tocantins (TO) - geocode: 1716109
* Londrina (PR) - geocode: 4113700
* Cambé (PR) - geocode: 4103701
* Cascavel (PR) - geocode: 4104808
* Aparecida de Goiânia (GO) - geocode: 5201405
* Campo Novo do Parecis (MT) - geocode: 5102637
* Novo Gama (GO) - geocode: 5215231


## Teams and models 

| Team | Institution | Country | Repository | Label in plots |
|------|-------------|---------|------------|---------------|
| Epidemáticos - Prophet | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_prophet | EMAP_PROPHET | 
| Epidemáticos - Sarimax | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_sarimax_muni | EMAP_SARIMAX | 
| NUS CERM| National University of Singapore | Singapore |https://github.com/SungmokJung/3rd_imdc_nus_nus-cerm| NUS-CERM| 
| XGBSillas | FGV-EMAP | Brazil | https://github.com/scrocha/3rd_imdc_emap_xgbsillas | EMAP_XGB |
| ISI Dengue | ISI Foundation | Italy | https://github.com/mattiamazzoli/3rd_imdc_isi_isi-dengue | ISI | 
| Dengue Oracle | FGV-EMAP | Brazil | https://github.com/eduardocorrearaujo/3rd_imdc_emap_lstm_muni | EMAP_LSTM | 
| Pattern-Blue | FGV-EMAP | Brazil | https://github.com/ZuilhoSe/3rd_imdc_fgv_pattern-blue | EMAP_BLUE | 
| Grupo Modelamiento de datos en Dengue | Universidad del Valle | Colombia | https://github.com/germanavila09/3rd_imdc_universidad_del_valle_grupo_modelamiento_datos_dengue | 
| Neural Earth | Purdue University | United States |https://github.com/kamrul28890/3rd_imdc_purdue_neuralearth | PURDUE | 
| Recogna | UNESP | Brazil | https://github.com/joel-da-silva-cavalcanti-filho/3rd_imdc_unesp_recogna | UNESP | 