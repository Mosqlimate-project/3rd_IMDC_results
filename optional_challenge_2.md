# 3rd Infodengue-Mosqlimate Dengue Challenge (IMDC): 2026 Sprint for dengue fever forecasts for Brazil

The Infodengue-Mosqlimate Dengue Challenge (IMDC) is an initiative led by the Mosqlimate and Infodengue. 

The objective of this 2026 sprint is **to promote training of predictive models and to develop high-quality ensemble forecast models for dengue in Brazil.**

The challenge involves four validation tests and one forecast target. The period of interest spans from the epidemiological week (EW) 41 of one year to EW 40 of the following year, aligning with the typical dengue season in Brazil.

**Validation test 1.** Predict the weekly number of dengue cases by state (UF) in the 2022-2023 season \[EW 41 2022- EW40 2023\], using data covering the period from EW 01 2010 to EW 25 2022;

**Validation test 2.** Predict the weekly number of dengue cases by state (UF) in the 2023-2024 season \[EW 41 2023- EW40 2024\], using data covering the period from EW 01 2010 to EW 25 2023;

**Validation test 3:** Predict the weekly number of dengue cases by state (UF) in the 2024-2025 season \[EW 41 2024- EW40 2025\], using data covering the period from EW 01 2010 to EW 25 2024;

**Validation test 4.** Predict the weekly number of dengue cases in Brazil, and by state (UF), in the 2025-2026 season \[EW 41 2025- EW40 2026\], using data covering the period from EW 01 2010 to EW 25 2025;

**Forecast.** Predict the weekly number of dengue cases in Brazil, and by state (UF), in the 2026-2027 season \[EW 41 2026- EW40 2027\], using data covering the period from EW 01 2010 to EW 25 2026;

The challenge workflow, from data release to the generation of the ensemble models, was identical to that of the first edition, as described by Araujo et al. (2026). In addition, this year, the competition included four forecasting challenges:

* **Mandatory Challenge – Dengue (State Level)**: Forecast dengue cases at the state (UF) level for all Brazilian states, except Espírito Santo.

* **Optional Challenge 1 – Dengue (City Level)**: Forecast dengue cases for 15 selected cities.

* **Optional Challenge 2 – Chikungunya (State Level)**: Forecast chikungunya cases at the state (UF) level for all Brazilian states, except Espírito Santo.

* **Optional Challenge 3 – Chikungunya (City Level)**: Forecast chikungunya cases for 10 selected cities.

This document presents the results for the **Optional Challenge 2 – Chikungunya (State Level)**. The results for the optional challenges are available in the following files:

* [Mandatory Challenge - Dengue state](readme.md).
* [Optional Challenge 1 - Dengue city](optional_challenge_1.md).
* [Optional Challenge 3 - Chikungunya city](optional_challenge_3.md).

# Results - Optional challenge 2: Chikungunya state level 

## Teams and models 

| Team | Institution | Country | Repository | Label in plots |
|------|-------------|---------|------------|---------------|
| Epidemáticos - Prophet | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_prophet | EMAP_PROPHET | 
| Epidemáticos - Sarimax | FGV EMAp | Brazil | https://github.com/EzequielEBS/3rd_imdc_emap_epidematicos_sarimax_state | EMAP_SARIMAX | 
| LNCC ARP26 | Laboratório Nacional de Computação Científica | Brazil | https://github.com/pesquefGH/3rd_imdc_lncc_lncc_arp26_chikungunya | LNCC_ARP26 |
| LNCC SURGE | Laboratório Nacional de Computação Científica | Brazil |https://github.com/pesquefGH/3rd_imdc_lncc_surge_model26_chikungunya | LNCC_SURGE | 
| NUS CERM| National University of Singapore | Singapore |https://github.com/SungmokJung/3rd_imdc_nus_nus-cerm| NUS-CERM| 
| XGBSillas | FGV-EMAP | Brazil | https://github.com/scrocha/3rd_imdc_emap_xgbsillas | EMAP_XGB |
| DS-OKSTATE-26 | Oklahoma State University | United States |https://github.com/haridas-das/DS-OKSTATE-2026| DS-OKSTATE| 
| BB model | PROCC | Brazil |https://github.com/lsbastos/3rd_imdc_procc_bb_model| PROCC| 
| Neural Earth | Purdue University | United States |https://github.com/kamrul28890/3rd_imdc_purdue_neuralearth | PURDUE | 
| LNCC CLIDENGO | Laboratório Nacional de Computação Científica | Brazil |https://github.com/americocunhajr/3rd_imdc_lncc_clidengo26chikungunya | LNCC_CLIDENGO | 
| Dengue Oracle | FGV-EMAP | Brazil | https://github.com/eduardocorrearaujo/3rd_imdc_emap_lstm | EMAP_LSTM | 


## Ranking and Scoring 

Model performance was evaluated using the **Weighted Interval Score (WIS)**, a proper scoring rule for probabilistic forecasts. To facilitate comparisons across models and states, we expressed the performance of each model relative to a baseline forecast by computing the ratio between its WIS and the WIS of a baseline model.

The baseline model adopted in this study was **PROCC (BB)** model, as described in Freitas et al. (2025). For each validation period (v), the relative performance was computed as

$$ R_v = \frac{\mathrm{WIS}{\mathrm{model},v}}{\mathrm{WIS}{\mathrm{baseline},v}}.$$

Values of **($R_v$ < 1)** indicate that the model **outperformed** the baseline, whereas values of **($R_v$ > 1)** indicate **inferior predictive performance**.

To summarize model performance across the four validation periods, we computed the **geometric mean** of ($R_v$) for each model within each state. Models were then ranked independently for each state according to this aggregated score, with lower values indicating better overall predictive performance.

The Weighted Interval Score was computed as

$$\mathrm{WIS}(F, y) =
\frac{1}{K + \tfrac{1}{2}}
\left(
w_0 |y - m|
+
\sum_{k=1}^{K}
w_k
S_{\alpha_k}^{\mathrm{int}}(l_k, u_k; y)
\right),$$

where ($y$) is the observed value, ($m$) is the predictive median, ($K$) is the number of prediction intervals, and ($l_k$) and ($u_k$) denote the lower and upper bounds of the (k)-th prediction interval with nominal level ($1-\alpha_k$), respectively. The interval weights are defined as ($w_k = \alpha_k/2$), while the median receives weight ($w_0 = 1/2$).

## Overall model performance relative to the baseline

### Scatter plot 

The figure below presents a scatter plot summarizing the overall performance of all submitted models across all states and validation periods. For each model, the (x)-axis represents the mean of ($\log(R_v)$), which is equivalent to the logarithm of the geometric mean of ($R_v$). The (y)-axis represents the standard deviation of ($\log(R_v)$), providing a measure of the variability of the model's relative performance across states and validation periods.

This visualization allows models to be classified into four performance regions:

* **Stable (green):** Models with a mean ($\log(R_v) < 0$), indicating that they outperform the baseline on average, and a standard deviation of ($\log(R_v)$) below the median, indicating relatively consistent performance across states and validation periods.

* **Better than the baseline, but inconsistent (blue):** Models with a mean ($\log(R_v) < 0$), indicating better average performance than the baseline, but with a standard deviation of ($\log(R_v)$) above the median, suggesting substantial variability in performance across states or validation periods.

* **Unstable (yellow):** Models with a mean ($\log(R_v) > 0$), indicating worse average performance than the baseline, and a standard deviation of ($\log(R_v)$) above the median, reflecting inconsistent performance across states or validation periods.

* **Consistently worse than the baseline (red):** Models with a mean ($\log(R_v) > 0$), indicating worse average performance than the baseline, and a standard deviation of ($\log(R_v)$) below the median, indicating consistently poor performance.

To improve readability, only models located in the **Stable** region are highlighted using distinct colors, as indicated in the legend. All remaining models are shown in gray.


![](figures/scatter_stable_chik_state.png)

### Violin plots 
In addition to the scatter plot, we generated violin plots to further characterize the distribution of ($R_v$) values across all models. The plots were produced using data from all Brazilian states combined as well as separately for each of the country's macro-regions.

These visualizations provide a more detailed view of the variability and central tendency of each model's relative performance. Models with a median ($R_v < 1$), indicating better median performance than the baseline, are shown in **green**. Models with a median ($R_v \geq 1$), indicating performance equal to or worse than the baseline, are shown in **blue**.

![](figures/violin_chik_state.png)

![](figures/violin_South_chik_state.png)

![](figures/violin_Southeast_chik_state.png)

![](figures/violin_Midwest_chik_state.png)

![](figures/violin_Northeast_chik_state.png)

![](figures/violin_North_chik_state.png)

## State performance 

### Heatmaps
To visualize model performance across states, we created the heatmap shown below. In this figure, each row represents a Brazilian state and each column represents a forecasting model. Each cell displays the geometric mean of (R_v) across the four validation periods for the corresponding state-model combination.

Cells are colored according to the model's relative performance: **green** indicates a geometric mean of (R_v < 0.95), corresponding to performance substantially better than the baseline; **white** indicates values between 0.95 and 1.05, corresponding to performance comparable to the baseline; and **red** indicates values greater than 1.05, corresponding to performance worse than the baseline.

Models are ordered from left to right according to the number of green cells, with the best-performing models appearing first. States are grouped by Brazilian macro-region to facilitate regional comparisons and highlight geographical patterns in model performance.

![](figures/matrix_BR_chik_state_T.png)

The value of this metric for each state and model is presented in this additional file [Supplementary Material](figures/sup_mat_dengue_state.md). 


As a complement to the heatmaps, we generated the figures below, considering only models with a geometric mean of ($R_v < 1$) for each state.

The first figure shows the number of states in which each model outperformed the baseline, providing an overall measure of model robustness across Brazil.

<img src="figures/n_states_out_base_by_model_chik_state.png" width="1000">

The second figure shows, for each state, the number of models that outperformed the baseline. This visualization helps identify states where accurate forecasting was more challenging, as indicated by a smaller number of models surpassing the baseline.

<img src="figures/n_models_out_base_by_state_chik_state.png" width="1000">

Based on these results, we selected **Paraná (PR)** and **Santa Catarina (SC)** for a more detailed analysis, as they were among the states where no models outperformed the baseline. The figures below compare the observed epidemic curves (black lines) with the forecasts from the baseline model. The baseline model is highlighted in a distinct color, while all remaining models are shown in gray.

<img src="figures/zoom_41_chik_state.png" width="1000">

<img src="figures/zoom_42_chik_state.png" width="1000">

The figure above are available for the other states
in this additional file [Supplementary Material](figures/sup_mat_chik_state.md).

### Best-performing models per state

The bar chart below shows the number of Brazilian states in which each model achieved the highest overall ranking, based on the geometric mean of the relative Weighted Interval Score ($R_v$) across the four validation periods.

![Best models by state](./figures/count_best_models_state_chik_state.png)

The map below illustrates the best-performing model in each state. States are colored according to the model that obtained the highest ranking, providing an overview of the geographical distribution of model performance across Brazil.

![Map best models by state](./figures/map_best_model_chik_state.png)

### Medal board 

The figures below summarize the top three models in each Brazilian macro-region. For every state, models were ranked according to the geometric mean of ($R_v$). 
#### South region: 

<img src="figures/medals_south_chik_state.png" width="500">

#### Southeast region: 

<img src="figures/medals_southeast_chik_state.png" width="500">

#### Midwest region: 

<img src="figures/medals_midwest_chik_state.png" width="500">

#### Northeast region: 

<img src="figures/medals_northeast_chik_state.png" width="1000">

#### North region: 

<img src="figures/medals_north_chik_state.png" width="1000">


## Performance by state - all validations 

To complement the overall analysis, the figures below illustrate model performance across the individual validation periods. In these plots, the y-axis represents the validation periods, while the x-axis displays the model ranking for each validation period. Each colored line corresponds to a different forecasting model, making it possible to assess the consistency of model performance over time and identify models whose rankings or relative performance vary substantially between validation periods.

<img src="figures/rankplot_52_rank_chik_state.png" width="1500">

The figure above presents the results for Goiás (GO). Equivalent visualizations for all other Brazilian states are provided in the [Supplementary Material](figures/sup_mat_chik_state.md).

## Epidemic characteristics

Additionally, using the copula-based approach described below, we transformed each model forecast into the parameters of a log-normal distribution. From these distributions, we generated 1,000 samples for each forecast and estimated four epidemic characteristics: the total number of cases, the maximum weekly number of cases (peak intensity), the peak week, and the epidemic onset week, together with their corresponding confidence intervals. The peak week and epidemic onset week were estimated by fitting a Richards growth model to the sampled trajectories, following the methodology proposed by Araujo et al. (2025).

The figures below present the distributions of the estimated epidemic characteristics for each validation period and forecasting model. In each histogram, the red dashed line indicates the observed value, while the blue bars represent the median estimate produced by each model. Results are shown beginning with Validation 2, as estimation of the copula parameter (\rho) requires information from the preceding validation period.

The figure below summarizes the estimated epidemic characteristics for Paraná (PR).

<img src="figures/hist_pars_41_chik_state.png" width="1500">


The results above correspond to Paraná (PR). Equivalent visualizations for all other Brazilian states are available in the [Supplementary Material](figures/sup_mat_chik_state.md).

## References 

Freitas, Laís Picinini, et al. "A statistical model for forecasting probabilistic epidemic bands for dengue cases in Brazil." Infectious Disease Modelling (2025).

Araujo, Eduardo C., et al. "Large-scale epidemiological modelling: scanning for mosquito-borne diseases spatio-temporal patterns in Brazil." Royal Society Open Science 12.5 (2025): 1-13.

Araujo, Eduardo C., et al. "Leveraging Probabilistic Forecasts for Dengue Preparedness and Control: The 2024 Dengue Forecasting Sprint in Brazil." Proceedings of the National Academy of Sciences of the United States of America, vol. 123, no. 7, 2026, e2508989123. https://doi.org/10.1073/pnas.2508989123.