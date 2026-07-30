# Supplementary Material - Optional Challenge 3 – Chikungunya City

## Heatmaps 

This supplementary document accompanies the main report and provides a detailed view of model performance relative to the baseline. Specifically, it presents the geometric mean of the relative performance metric ($R_v$) computed across the four validation periods for each model and city.


![](heatmap__chik_city.png)


## Times series 

The figures below compare the observed epidemic curves (black lines) with forecasts from the baseline model and the models that achieved better performance than the baseline. These models are highlighted using distinct colors, while all remaining models are shown in gray.

### Cascavel (PR)
<img src="zoom_4104808_chik_city.png" width="1000">

### Xanxerê (PR)
<img src="zoom_4219507_chik_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="zoom_3119401_chik_city.png" width="1000">

### Montes Claros (MG)
<img src="zoom_3143302_chik_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="zoom_5102637_chik_city.png" width="1000">

### Cuiabá (GO)
<img src="zoom_5103403_chik_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="zoom_2931350_chik_city.png" width="1000">

### Teresina (PI)
<img src="zoom_2211001_chik_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="zoom_1716109_chik_city.png" width="1000">

### Palmas (TO)
<img src="zoom_1721000_chik_city.png" width="1000">

## Rankplots 

The figures below illustrate model performance across the individual validation periods. In these plots, the y-axis represents the validation periods, while the x-axis displays the model ranking for each validation period. Each colored line corresponds to a different forecasting model, making it possible to assess the consistency of model performance over time and identify models whose rankings or relative performance vary substantially between validation periods.


### Cascavel (PR)
<img src="rankplot_4104808_rank_chik_city.png" width="1000">

### Xanxerê (PR)
<img src="rankplot_4219507_rank_chik_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="rankplot_3119401_rank_chik_city.png" width="1000">

### Montes Claros (MG)
<img src="rankplot_3143302_rank_chik_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="rankplot_5102637_rank_chik_city.png" width="1000">

### Cuiabá (GO)
<img src="rankplot_5103403_rank_chik_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="rankplot_2931350_rank_chik_city.png" width="1000">

### Teresina (PI)
<img src="rankplot_2211001_rank_chik_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="rankplot_1716109_rank_chik_city.png" width="1000">

### Palmas (TO)
<img src="rankplot_1721000_rank_chik_city.png" width="1000">


## Epidemic characteristics


The figures below present the distributions of the estimated epidemic characteristics (the total number of cases, the maximum weekly number of cases (peak intensity), the peak week, and the epidemic onset week) for each validation period and forecasting model. In each histogram, the red dashed line indicates the observed value, while the blue bars represent the median estimate produced by each model. Results are shown beginning with Validation 2, as estimation of the copula parameter (\rho) requires information from the preceding validation period.

### Cascavel (PR)
<img src="hist_pars_4104808_chik_city.png" width="1000">

### Xanxerê (PR)
<img src="hist_pars_4219507_chik_city.png" width="1000">

### Coronel Fabriciano (MG)
<img src="hist_pars_3119401_dengue_city.png" width="1000">

### Montes Claros (MG)
<img src="hist_pars_3143302_chik_city.png" width="1000">

### Campo Novo do Parecis (MT)
<img src="hist_pars_5102637_chik_city.png" width="1000">

### Cuiabá (GO)
<img src="hist_pars_5103403_chik_city.png" width="1000">

### Teixeira de Freitas (BA)
<img src="hist_pars_2931350_chik_city.png" width="1000">

### Teresina (PI)
<img src="hist_pars_2211001_chik_city.png" width="1000">

### Paraíso do Tocantins (TO)
<img src="hist_pars_1716109_chik_city.png" width="1000">

### Palmas (TO)
<img src="hist_pars_1721000_chik_city.png" width="1000">