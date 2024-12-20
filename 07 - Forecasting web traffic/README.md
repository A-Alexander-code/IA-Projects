# Web Traffic Forecasting with Exogenous Features

## Introduction
In this project, I develop an autoregressive model to forecast web traffic using historical data. The model, named ForecasterAutoreg, employs a linear regressor with Ridge regularization. This approach leverages a time window of 14 days, meaning that for each prediction, the web traffic data from the previous two weeks is used as predictors.

To ensure the effectiveness of the Ridge regression model, which requires standardized predictors, a StandardScaler is incorporated into the forecasting pipeline. This standardization is achieved by adding the scaler to the forecaster through the transformer_y argument. By doing so, the model benefits from improved stability and performance, providing more accurate predictions of future web traffic trends.

This combination of autoregressive modeling and standardization techniques allows us to create a robust framework for anticipating web traffic patterns, helping to inform decision-making processes and optimize resource allocation.

## Overview
This repository contains code for forecasting web traffic using two different methods: `forecasterAutoreg` and ARIMA with exogenous features. The dataset used for this purpose is `visitas_por_dia_web_cienciadedatos.csv`.

## Dataset
The dataset `visitas_por_dia_web_cienciadedatos.csv` contains daily web traffic data for a website related to data science. It includes the following columns:
- Date: The date of the recorded data.
- Visits: The number of visits to the website on that particular date.

## Methods
### 1. forecasterAutoreg
`forecasterAutoreg` is a forecasting method that utilizes autoregressive modeling. It is implemented using Python's `forecasterAutoreg` library.

### 2. ARIMA with Exogenous Features
ARIMA (Autoregressive Integrated Moving Average) with exogenous features is a statistical method for time series forecasting that incorporates external variables (exogenous features) in addition to the time series data.


## Results
The results of the forecasting methods will be saved in the `results` section.

## Conclusion
This project demonstrates the use of two different methods, `forecasterAutoreg` and ARIMA with exogenous features, for forecasting web traffic based on the provided dataset. Users can compare the performance of these methods and choose the one that best suits their needs.

For any questions or issues, please contact [b_alx_arboleda@outlook.com].