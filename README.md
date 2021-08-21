# Project 5

## Executive Summary

**Do you have any ideas on climate change and how it affects the environment?** Climate change is the long-term alteration of temperature and typical weather patterns in a geographical location. The main reason behind this change is the emission of excess amounts of greenhouse gases which causes global warming. One of the most adverse effects of global warming is **rising sea levels.**

The change in sea level includes risks such as frequent floods in coastal areas where the weather stations might be located. It also affects oil and gas companies that deal with offshore oil rigs. It will have its worst effects on commercial fishing and insurance companies. All you need is to have a better understanding of the geographical features of coastal areas. This will prevent potentially catastrophic losses.

The challenge is, how to determine the sea levels proximate to the weather stations. We seek to explore this in this project through data science methods in creating an optimal model for sea level prediction. Data can be gathered from tide stations and satellite data. 

There is always a solution. The best possible way to predict sea-level change is to study the patterns in the past and the patterns in similar and nearby locations. To achieve this, we built a machine learning model which uses the Random Forest Model that gives a RMSE (root mean square error) of 193.00 cm. 

As a state with rich resources, industries such as the oil and gas fields should consider setting up offshore rigs in a resourceful place where there will be no significant change in sea level to affect the process in the long term. This keeps Alaska's residents safe while keeping its economy significant.

We love to collaborate with an esteemed organization like yours. We will help you to minimize the risks caused by sea-level change throughout the state.


## Overview

## Datasets

|File Name|Organization|Dataset Location|Description|
|---|---|---|---|
|**2682403.csv**|[National Centers for Environmental Information (National Oceanic and Atmospheric Administration)](https://www.ncdc.noaa.gov/cdo-web/)|[Information Request](https://www.ncdc.noaa.gov/cdo-web/orders?email=akira.j.takahashi@gmail.com&id=2682403)|Daily Summaries for various weather stations in Alaska|
|**co2_brw_surface-insitu_1_ccgg_DailyData.txt**|[National Centers for Environmental Information (National Oceanic and Atmospheric Administration)](https://www.ncdc.noaa.gov/cdo-web/)|[Data source](https://gml.noaa.gov/aftp/data/trace_gases/co2/in-situ/surface/brw/co2_brw_surface-insitu_1_ccgg_DailyData.txt)|Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous measurements at Barrow, Alaska|
|**Dutch.csv** </br> **Ketchikan.csv** </br> **Kodiak.csv** </br> **Nome.csv** </br> **Seward.csv** </br> **Sitka.csv** </br> **Yakutat.csv**|[University of Hawaii Sea Level Center](https://uhslc.soest.hawaii.edu)|[Link to Dataset](http://uhslc.soest.hawaii.edu/data/)|Sealevels for various weather stations in Alaska|

## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**LONGITUDE**|*type*|Dataset|Decimated degrees w/western hemisphere values < 0, eastern hemisphere values > 0
|**ELEVATION**|*type*|Dataset|Elevation above mean sea level (tenths of meters)
|**TMIN**|*float*|Dataset|Minimum Temperature (Celsius)
|**TMAX**|*float*|Dataset|Maximum Temperature (Celsius)
|**PRCP**|*float*|Dataset|Precipitation (millimeters)
|**TAVG**|*float*|Dataset|Average Temperature (Celsius)



## Data Cleaning

## EDA

## Modeling


|**Model**|Features|R-squared score (Training)|R-squared score (Testing)|CV Score|RMSE|Description|
|---|---|---|---|---|---|---|
|**Machine Learning**|---|---|---|---|---|---|---|
|Simple Linear Regression (baseline)|---|---|---|0.7670867255188408|443.97424986525846|---|
|Linear Regression (Best 5 Features)|---|0.5807322845500629|0.5839589834509318|---|655.1519185205403|---|
|Linear Regression with Polynomial Features|---|---|---|0.9519478687000185|---|---|
|Random Forest|Top 5 correlated|0.9898934248180209|0.9639127264658994|---|192.9527525951641|---|
|Extra Trees|Top 5 correlated|0.9932009532429776|0.9602867753024416|---|202.4144530052038|---|
|ADA Boosting|Top 5 correlated|0.9602476538870952|0.9600125174491985|---|203.11218328755675|---|
|**Deep Learning**|---|---|---|---|---|---|---|
|Neural Net Model|Top 5 correlated|---|---|---|771.5795010341686|---|
|Neural Net Model|All|---|---|---|---|---|
|Neural Net Model (GridSearch)|Top 5 correlated|---|---|0.9281423319609716|272.1333481297308|Best Parameters <br />  dropout: 0.1 <br />  epochs: 30, <br />  hidden_layers: 5, <br />  hidden_neurons: 64|
|Neural Net Model (GridSearch)|All|---|---|---|---|---|
|Recurrent Neural Net Model|Top 5 correlated|---|---|---|---|---|
|Recurrent Neural Net Model|All|---|---|---|---|---|


## Analysis


## Summary

In this study, we looked to build a machine learning model that can accurately predict the sea level in the greater Alaskan coast given certain meteorological parameters. When building these models, we used the Root Mean Squared Error (RMSE) as an evaluation metric since it helps us compare the performance of our models predictions. Our baseline score was an RMSE of 443.97, which resulted from a multiple linear regression using all of our initial features. The Random Forest model ended up performing the best with an RMSE of 192.9, which is a marked improvement on our baseline by a ~2.3x. In addition to this, the Random Forest model had a R-squared score of 98.98% on the training data and a R-squared score of 96.39% on the testing data. Unsurprisingly, the R-squared score on the testing data was the highest among our different models. We recommend regulators use our Random Forest model for predicting sea level due to its low RMSE and high R-squared score. 

Random Forest models offer a level of interpretability over say black-box models like the recurrent neural network (RNN) model we trained, in addition to being more cost-effective and simpler in training. We are able to extract our feature importances form our Random Forest model and we found Elevation and Longitude to be the more important features in predicting the sea level in Alaska. In terms of interpretation, this makes sense in that the innate elevation of each weather station will play a large part in determing the sea level. Sea level is read using tide gauges which have a zero-reference for each given station, or rather a fixed base elevation at a tide station to which all water level measurements are referred. In conjunction with latitude, the geographic location of each tide station played the largest part in mapping its sea level. 

Climate change data was included in our dataset as atmospheric Carbon Dioxide (CO2) Dry Air Mole fractions, recorded by the Barrow Atmospheric Baseline Observatory (BRW) located in Utqiaġvik, Alaska. The readings from the BRW are characterized as 'having an Arctic maritime climate affected by variations of weather and sea ice conditions in the Central Arctic' due to its close proximity to the Arctic Ocean. Despite our presumptions regarding Carbon Dioxide and rising sea level due to its trapping of heat, we found there was almost no correlation between the atmospheric CO2 in BRW and the sea level from our weather stations. Interestingly enough, portions of Alaska have *decreasing* sea levels due to a process called glacial isostatic adjustment. This is the process where even if melting ice sheets in Alaska are contributing to sea level rise across the globe, the volume of ice melt actually leads to a decrease in sea levels off the Alaskan coast. Think of the ice in Alaska's land as a moon with its own gravitational pull.. as the moon itself loses mass, the gravitational pull will be weaker which will then lead to lowered sea levels around Alaska. This may explain why atmospheric CO2 concentration did not play a large part in our models. 

With this in mind, in further studies, it is recommended to make predictions using isolated station data since their location (latitude and elevation) played such a large part in the predictive power of our models. If doing so, it would be recommended to use more frequent data observations such as hourly average when it comes to sea level to increase the overall sample population. Future studies should account for the glacial isostatic adjustment in Alaska which makes it such a unique area to study in regards to sea level rise. We would also recommend recording new station data around the Alaskan coast. There was a lack of historical data from coastlines in the northeast and northern regions of Alaska, with which if more station points were available, could only improve future models by having a wealth of data points tied around different elevations. Finally, incorporating a diverse set of features such as sea surface salinity, sea surface temperature, and mean sea level pressure (2020, Sithara) would further enhance research into this area. 

