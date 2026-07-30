# Supplementary Material - Optional Challenge 1 – Dengue City

## Heatmaps 

This supplementary document accompanies the main report and provides a detailed view of model performance relative to the baseline. Specifically, it presents the geometric mean of the relative performance metric ($R_v$) computed across the four validation periods for each model and city.


![](heatmap__dengue_city.png)


## Times series 

The figures below compare the observed epidemic curves (black lines) with forecasts from the baseline model and the models that achieved better performance than the baseline. These models are highlighted using distinct colors, while all remaining models are shown in gray.

### Londrina (PR)
<img src="zoom_4113700_dengue_city.png" width="1000">

### Cambé (PR)
<img src="zoom_4103701_dengue_city.png" width="1000">

### Cascavel (PR)
<img src="zoom_4104808_dengue_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="zoom_3119401_dengue_city.png" width="1000">

### São José do Rio Preto (SP)
<img src="zoom_3549805_dengue_city.png" width="1000">

### Presidente Prudente (SP)
<img src="zoom_3541406_dengue_city.png" width="1000">

### Aparecida de Goiânia (GO)
<img src="zoom_5201405_dengue_city.png" width="1000">

### Novo Gama (GO)
<img src="zoom_5215231_dengue_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="zoom_5102637_dengue_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="zoom_2931350_dengue_city.png" width="1000">

### Vitória da Conquista (BA)
<img src="zoom_2933307_dengue_city.png" width="1000">

### Brejo Santo (CE)
<img src="zoom_2302503_dengue_city.png" width="1000">

### Rio Branco (AC)
<img src="zoom_1200401_dengue_city.png" width="1000">

### Cruzeiro do Sul (AC)
<img src="zoom_1200203_dengue_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="zoom_1716109_dengue_city.png" width="1000">

## Rankplots 

The figures below illustrate model performance across the individual validation periods. In these plots, the y-axis represents the validation periods, while the x-axis displays the model ranking for each validation period. Each colored line corresponds to a different forecasting model, making it possible to assess the consistency of model performance over time and identify models whose rankings or relative performance vary substantially between validation periods.


### Londrina (PR)
<img src="rankplot_4113700_rank_dengue_city.png" width="1000">

### Cambé (PR)
<img src="rankplot_4103701_rank_dengue_city.png" width="1000">

### Cascavel (PR)
<img src="rankplot_4104808_rank_dengue_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="rankplot_3119401_rank_dengue_city.png" width="1000">

### São José do Rio Preto (SP)
<img src="rankplot_3549805_rank_dengue_city.png" width="1000">

### Presidente Prudente (SP)
<img src="rankplot_3541406_rank_dengue_city.png" width="1000">

### Aparecida de Goiânia (GO)
<img src="rankplot_5201405_rank_dengue_city.png" width="1000">

### Novo Gama (GO)
<img src="rankplot_5215231_rank_dengue_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="rankplot_5102637_rank_dengue_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="rankplot_2931350_rank_dengue_city.png" width="1000">

### Vitória da Conquista (BA)
<img src="rankplot_2933307_rank_dengue_city.png" width="1000">

### Brejo Santo (CE)
<img src="rankplot_2302503_rank_dengue_city.png" width="1000">

### Rio Branco (AC)
<img src="rankplot_1200401_rank_dengue_city.png" width="1000">

### Cruzeiro do Sul (AC)
<img src="rankplot_1200203_rank_dengue_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="rankplot_1716109_rank_dengue_city.png" width="1000">



## Epidemic characteristics


The figures below present the distributions of the estimated epidemic characteristics (the total number of cases, the maximum weekly number of cases (peak intensity), the peak week, and the epidemic onset week) for each validation period and forecasting model. In each histogram, the red dashed line indicates the observed value, while the blue bars represent the median estimate produced by each model. Results are shown beginning with Validation 2, as estimation of the copula parameter (\rho) requires information from the preceding validation period.

### Londrina (PR)
<img src="hist_pars_4113700_dengue_city.png" width="1000">

### Cambé (PR)
<img src="hist_pars_4103701_dengue_city.png" width="1000">

### Cascavel (PR)
<img src="hist_pars_4104808_dengue_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="hist_pars_3119401_dengue_city.png" width="1000">

### São José do Rio Preto (SP)
<img src="hist_pars_3549805_dengue_city.png" width="1000">

### Presidente Prudente (SP)
<img src="hist_pars_3541406_dengue_city.png" width="1000">

### Aparecida de Goiânia (GO)
<img src="hist_pars_5201405_dengue_city.png" width="1000">

### Novo Gama (GO)
<img src="hist_pars_5215231_dengue_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="hist_pars_5102637_dengue_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="hist_pars_2931350_dengue_city.png" width="1000">

### Vitória da Conquista (BA)
<img src="hist_pars_2933307_dengue_city.png" width="1000">

### Brejo Santo (CE)
<img src="hist_pars_2302503_dengue_city.png" width="1000">

### Rio Branco (AC)
<img src="hist_pars_1200401_dengue_city.png" width="1000">

### Cruzeiro do Sul (AC)
<img src="hist_pars_1200203_dengue_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="hist_pars_1716109_dengue_city.png" width="1000">