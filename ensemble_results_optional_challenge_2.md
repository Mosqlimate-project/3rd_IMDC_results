# 3rd Infodengue-Mosqlimate Dengue Challenge (IMDC)
## Ensemble Models Results

**Organization:**  
![](figures/infodengue_mosqlimate.png)

**Funding:**  
<img src="figures/Wellcome_Trust_logo.png" width="  100" />

This file presents the results of the ensemble forecasts generated from submitted chikungunya forecasting models for the state-level **optional challenge 2** of the 2026 IMDC.

---


## Teams and models

Of the 12 models submitted for the chikungunya state-level challenge, one was designated as the baseline, leaving 11 models for analysis. The models included in the analysis are listed in the table below. **The BB model was used as the baseline for comparison.**


| Team | Institution | Country | Repository | Label in plots |
|------|-------------|---------|------------|---------------|
| Epidemáticos - Prophet* | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_prophet_fixed | EMAP_PROPHET | 
| Epidemáticos - Sarimax* | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_sarimax_fixed | EMAP_SARIMAX | 
| LNCC ARP26 | Laboratório Nacional de Computação Científica | Brazil | https://github.com/pesquefGH/3rd_imdc_lncc_lncc_arp26_chikungunya | LNCC_ARP26 |
| LNCC SURGE | Laboratório Nacional de Computação Científica | Brazil |https://github.com/pesquefGH/3rd_imdc_lncc_surge_model26_chikungunya | LNCC_SURGE | 
| NUS CERM| National University of Singapore | Singapore |https://github.com/SungmokJung/3rd_imdc_nus_nus-cerm| NUS-CERM| 
| XGBSillas | FGV-EMAP | Brazil | https://github.com/scrocha/3rd_imdc_emap_xgbsillas | EMAP_XGB |
| DS-OKSTATE-26 | Oklahoma State University | United States |https://github.com/haridas-das/DS-OKSTATE-2026| DS-OKSTATE| 
| BB model | PROCC | Brazil |https://github.com/lsbastos/3rd_imdc_procc_bb_model| PROCC| 
| Neural Earth | Purdue University | United States |https://github.com/kamrul28890/3rd_imdc_purdue_neuralearth | PURDUE | 
| LNCC CLIDENGO | Laboratório Nacional de Computação Científica | Brazil |https://github.com/americocunhajr/3rd_imdc_lncc_clidengo26chikungunya | LNCC_CLIDENGO | 
| Dengue Oracle | FGV-EMAP | Brazil | https://github.com/eduardocorrearaujo/3rd_imdc_emap_lstm | EMAP_LSTM | 
| Mosqlimate AI | FGV-EMAP | Brazil | https://github.com/fccoelho/mosqlimate-ai-competitor | EMAP_TIMESFM |

*The validation forecasts for these models have been updated following the identification of inconsistencies in the workflow used to generate them.

---

## The Ensemble

### Model Ranking Methodology 

Model performance was evaluated using the ratio between each model's **Weighted Interval Score (WIS)** and the WIS of a **baseline model**.

For each validation period $v$, the performance ratio was computed as

$$R_v = \frac{\mathrm{WIS}_{\mathrm{model},v}}
{\mathrm{WIS}_{\mathrm{baseline},v}}.$$

* $R_v < 1$: model outperforms the baseline.
* $R_v > 1$: model performs worse than the baseline.

To obtain a single score for each state, the **geometric mean** of $R_v$ across the four validation periods was computed. Models were then ranked within each state according to this value, with **lower values indicating better predictive performance**.

### Forecast Puzzle

The figure below shows, for each row, the rank of the model corresponding to the column name within each validation set, based on the geometric mean of the wis ratio. For each state, the model with the lowest geometric average across the four validation periods was selected (column name). The figure illustrates that model performance can vary between validation years, as observed for states such as MG and BA. This lack of consistency in model performance, combined with the limited number of validation samples, informed the methodology used for constructing the ensemble.

![Ranking of best models](figures/forecast_puzzle_chik_state.png)  


---

### Ensemble Method

Following the [COVID Hub methodology](https://doi.org/10.1016/j.ijforecast.2022.06.005) we computed the median of predictive intervals from each model. Since the results were similar to those obtained from logarithmic pooling with equal weights, we opted for the **median**, which does not need a parametric approximation.

---

### Inclusion Criteria

Evaluating Ensemble Performance as a Function of Size

* Analyzed changes in the WIS ratio between the ensemble and the baseline as the top (K) models were progressively added, ranked by performance in previous validation seasons.

* Conducted the analysis separately for each validation set.

* Summarized results by plotting the proportion of state–validation set pairs in which the ensemble outperformed the baseline $(\mathrm{WIS}_{\text{ensemble}} / \mathrm{WIS}_{\text{baseline}} < 1)$ for each ensemble size (K).

In the figure below, each line represents a state. The x-axis shows the number of models included in the ensemble, while the y-axis shows the WIS ratio between the ensemble and the baseline. Models are added in order of their performance on previous validation sets.

![](figures/wis_ratio_top_k_validations_chik_state.png)  


To summarize the results shown in the figure above, we calculated, for each ensemble size, the proportion of state–validation pairs for which the WIS ratio between the ensemble and the baseline was below 1, indicating better performance by the ensemble. This analysis was used to determine a cutoff for the number of models to include in the ensemble. Based on these results, we selected the **top 10 models for inclusion in the ensemble**.

![](figures/wis_ratio_top_k_agg_chik_state.png)  


---

## Results

#### Brazil (National)

The figure below presents the median and confidence interval of 90% of the total cases computed for the 2026-2027 season against the number of cases notified up to EW 202639.

![](figures/cum_inc_2027_en_chik_state_log.png)


The map and table below show, by state, the percentage ratio between the cumulative incidence predicted by the median of the ensemble model (2026-2027 season) and the cumulative incidence observed during the 2025-2026 season.

![](figures/map_table_inc_2027_chik_state.png)


### Regional Results

The panels below show results for each state, grouped by macroregion. In each section, the first panel represents the weekly incidence, and the second panel shows the cumulative incidence. Within the panels, the median ensemble predictions are displayed as dashed blue lines, the median predictions of the best model for each state as solid red lines, predictions from the other models as solid grey lines, and the incidence from the previous season as dotted black lines. The cumulative incidence was computed by summing the median predictions; therefore, it does not include prediction intervals.

#### South Region
![](figures/weekly_cases_sul_en_chik_state.png)  
![](figures/cumulative_cases_sul_en_chik_state.png)

#### Southeast Region
![](figures/weekly_cases_sudeste_en_chik_state.png)  
![](figures/cumulative_cases_sudeste_en_chik_state.png)

#### Midwest Region
![](figures/weekly_cases_centro_oeste_en_chik_state.png)  
![](figures/cumulative_cases_centro_oeste_en_chik_state.png)

#### Northeast Region
![](figures/weekly_cases_nordeste_en_chik_state.png)  
![](figures/cumulative_cases_nordeste_en_chik_state.png)

#### North Region
![](figures/weekly_cases_norte_en_chik_state.png)  
![](figures/cumulative_cases_norte_en_chik_state.png)


---

### Important Dates

> **Save these dates!**
> 1. Webinar presenting results for the Brazilian Ministry of Health — **November 06, 2026**

