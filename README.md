# Assessment of Sealevel rise in Alaska given Current climate change

## Executive Summary

**Do you understand how climate change affects the environment?** Climate change is the long-term alteration of temperature and typical weather patterns in a geographical location. The main reason behind this change is the emission of excess amounts of greenhouse gases which causes global warming. One of the most adverse effects of global warming is **rising sea levels.**

The change in sea level includes risks such as frequent floods in coastal areas where the weather stations might be located. It also affects oil and gas companies that deal with offshore oil rigs. It will have its worst effects on commercial fishing and insurance companies. All you need is to have a better understanding of the geographical features of coastal areas. This will prevent potentially catastrophic losses.

The challenge is, how to determine the sea levels proximate to the weather stations. We seek to explore this in this project through data science methods in creating an optimal model for sea level prediction. Data was be gathered from tide (weather) stations and satellite data from two prestigious organizations, the National Oceanic and Atmospheric Administration, as well as the University of Hawaii Sea Level Center. 

There is always a solution. The best possible way to predict sea-level change is to study the patterns in the past and the patterns in similar and nearby locations. To achieve this, we built a machine learning model which uses the Random Forest Model that gives a RMSE (root mean square error) of 193.00 cm. 

As a state with rich resources, industries such as the oil and gas fields should consider setting up offshore rigs in a resourceful place where there will be no significant change in sea level to affect the process in the long term. This keeps Alaska's residents safe while keeping its economy significant.

We would love to collaborate with entities that promote preserving our planet's climate. We will help you to minimize the risks caused by sea-level change throughout the state of Alaska.


## Overview

The purpose of our project is to create an optimal model to predict sea levels in various geographical areas of Alaska to pinpoint areas requiring attention from environmental regulators.
We would like to pitch this to the below two environmental regulators:
- Alaska Department of Environmental Conservation - State level agency
- Environmental Protection Agency (EPA) - National level agency

Rising seas threaten infrastructure necessary for local jobs, and regional industries. These infrastructures include but are not limited to roads, bridges, subways, water supplies, oil and gas wells, power plants, sewage treatment plants, landfills.

Almost 40% of of US population lives in relatively high-population density coastal areas, and 8 of the world's 10 largest cities are in close proximity to an ocean.

In this study, in this study, we attempt to explore the most important features in predicting sea levels in Alaska.
Initially, we had started working on this project with the expectation of Carbon Dioxide being a major factor in sea levels. Carbon Dioxide is a greenhouse gas (a gas that absorbs and radiates heat, traps heat and raises the Earth's average temperature). However, we soon came to realize that the atmospheric Carbon Dioxide in Alaska does not play a major role, at least based on the limited information we obtained from the NOAA.

We collected data for individual weather stations scattered across Alaska, as well as their respective area's sea level information.

## Directory

- **Clean_dataframe folder**
    - **clean_df.csv :** The final dataframe resulting from data cleaning that we performed
- **data dictionaries**
    - **noaa_co2.md :** Simple reference guide for the Carbon Dioxide data from NOAA
    - **noaa_daily_summ.md:** Reference guide for daily summaries obtained from NOAA
    - **univ_hawaii_sealevel.md:** Reference guide for University of Hawaii sea level dataset
- **data folder**
    - **site folder:** The sea level data for each weather station (from University of Hawaii)
    - **station_points.csv:** The coordinates of each weather station (pulled from NOAA for Tableau app)
    - **tl_2020_us_state:** Tableau files
    - **2682403.csv:** Daily summary data collected from NOAA for each weather station
    - **cleaned_co2_data.txt:** Cleaned version of co2 data (below) by removing excess comments from .txt file
    - **co2_brw_surface-insitu_1_ccgg_DailyData.txt:** Raw Carbon Dioxide data collected from NOAA
    - **station_points.csv:** Geography information (latitude, longitude, geometry) for each weather station created from NOAA data for Tableau input
- **Draft files** - files used in our project but not part of our final deliverables. Kept for reference (possibly expanding on geopandas plotting in the future)
- **st_images** - streamlit app images
- **Notebooks:**
    - 01_data_cleaning_EDA_ML_models.ipynb
    - 02-deep_learning_6features.ipynb
    - 03-deep_learning_all_features.ipynb
    - 04_Conclusion_and_Recommendations.ipynb
    - 05_Streamlit_app_memo.ipynb
- **Alaska Sea Level Rise Presentation Slides.pdf**
- **README.md**
- **st-app.py** - Streamlit app. **Note, please run contents of notebook 01, and read notebook 05 before running streamlit app**

    
## Datasets

|File Name|Organization|Dataset Location|Description|
|---|---|---|---|
|**2682403.csv**|[National Centers for Environmental Information (National Oceanic and Atmospheric Administration)](https://www.ncdc.noaa.gov/cdo-web/)|[Information Request](https://www.ncdc.noaa.gov/cdo-web/orders?email=akira.j.takahashi@gmail.com&id=2682403)|Daily Summaries for various weather stations in Alaska|
|**co2_brw_surface-insitu_1_ccgg_DailyData.txt**|[National Centers for Environmental Information (National Oceanic and Atmospheric Administration)](https://www.ncdc.noaa.gov/cdo-web/)|[Data source](https://gml.noaa.gov/aftp/data/trace_gases/co2/in-situ/surface/brw/co2_brw_surface-insitu_1_ccgg_DailyData.txt)|Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous measurements at Barrow, Alaska|
|**Dutch.csv** </br> **Ketchikan.csv** </br> **Kodiak.csv** </br> **Nome.csv** </br> **Seward.csv** </br> **Sitka.csv** </br> **Yakutat.csv**|[University of Hawaii Sea Level Center](https://uhslc.soest.hawaii.edu)|[Link to Dataset](http://uhslc.soest.hawaii.edu/data/)|Sealevels for various weather stations in Alaska|

## Data Dictionary

We determined from preparing a correlation heatmap and comparing between all variables and sea level, and determined the below 6 features to be the most correlated.
- Longitude
- Elevation
- Minimum Temperature
- Maximum Temperature
- Average Temperature
- Precipitation

Based on this, we refer to these features most used in our modeling in our data dictionary below.

For remaining variables, please refer to the *data dictionary* directory for the Station Data Dictionary info, and Daily Summary info.
More information can be obtained through each organization's website (see **Datasets**)

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**LONGITUDE**|*type*|Dataset|Decimated degrees w/western hemisphere values < 0, eastern hemisphere values > 0
|**ELEVATION**|*type*|Dataset|Elevation above mean sea level (tenths of meters)
|**TMIN**|*float*|Dataset|Minimum Temperature (Celsius)
|**TMAX**|*float*|Dataset|Maximum Temperature (Celsius)
|**PRCP**|*float*|Dataset|Precipitation (millimeters)
|**TAVG**|*float*|Dataset|Average Temperature (Celsius)

## Data Cleaning

In this project, we spent significant time doing research by reading and understanding climate data, and ultimately cleaning and merging 3 separate data sets (TWO from the National Oceanic and Atmospheric Administration - each pertaining to daily summaries of weather stations and Carbon Dioxide, respectively, and ONE from the University of Hawaii Sea Level Center for the sea level at each weather station).
    - We chose the weather stations in the NOAA that had sea level data from the University of Hawaii

- Data Cleaning Techniques Used:
    - Checking for null values
    - Confining our project timeframe from January 1, 1980 to December 31, 2020
    - Reading in Carbon Dioxide data from NOAA
        - Reading in a .txt file and editing to make into a presentable dataframe
        - Renaming columns and creating data columns consistent with the NOAA daily summaries data to merge dataframes together
    - Checking for unique values for each weather/climate attribute in the NOAA data, and filling with 0s, nulls or medians as we saw appropriate
    - Renaming columns and numerifying categorical variables to include in our regression model
    - Merging weather station information (e.g. Latitude and Longitude)


## EDA

- Histograms of Sea level plots to determine distribution in the data we obtained


- Boxplots and Scatterplots of the 6 most correlated features against sea level

## Modeling

We created a total of 10 models, and summarize our results below.
We used correlation coefficients and root mean squared error values as metrics for our comparison.

Upon completion of our modeling, we found that while Random Forest fit the training data slightly worse than our Extra Trees on our training data, the Random Forest Model had the best correlation coefficient for the test set values and root mean squared error values overall.

Because the traditional Machine Learning models (as opposed to the Deep Learning models)' Python code compiled significantly faster, and performed better, we decided to use the Random Forest model for our final model.

||**Model**|Features|R-squared score (Training)|R-squared score (Testing)|RMSE|Description|
|---|---|---|---|---|---|---|
||**Machine Learning**|---|---|---|---|---|
|1|Simple Linear Regression (baseline)|All|---|0.7670867255188408|443.97424986525846|---|
|2|Simple Linear Regression (baseline)|Best 6 Features|0.5807322845500629|0.5839589834509318|655.1519185205403|---|
|3|Linear Regression with Polynomial Features|All + Newly created polynomial features|---|0.9519478687000185|---|---|
|4|Random Forest|Best 6 Features|0.9898934248180209|0.9639127264658994|192.9527525951641|---|
|5|Extra Trees|Best 6 Features|0.9932009532429776|0.9602867753024416|202.4144530052038|---|
|6|ADA Boosting|Best 6 Features|0.9602476538870952|0.9600125174491985|203.11218328755675|---|
||**Deep Learning**|---|---|---|---|---|
|7|Neural Net Model|Best 6 Features|---|0.33055759362671944|830.6189120511758|---|
|8|Neural Net Model (GridSearch)|Best 6 Features|---|0.9632379393231948|194.6458412454534|Best Parameters <br />  dropout: 0.1 <br />  epochs: 50, <br />  hidden_layers: 5, <br />  hidden_neurons: 64|
|9|Recurrent Neural Net Model|Best 6 Features|---|---|274.592226037|---|
|10|Recurrent Neural Net Model|Best 6 Features|---|---|1053.94425849|Early Stopping|

## Summary

In this study, we looked to build a machine learning model that can accurately predict the sea level in the greater Alaskan coast given certain meteorological parameters. When building these models, we used the Root Mean Squared Error (RMSE) as an evaluation metric since it helps us compare the performance of our models predictions. Our baseline score was an RMSE of 443.97, which resulted from a multiple linear regression using all of our initial features. The Random Forest model ended up performing the best with an RMSE of 192.9, which is a marked improvement on our baseline by a ~2.3x. In addition to this, the Random Forest model had a R-squared score of 98.98% on the training data and a R-squared score of 96.39% on the testing data. Unsurprisingly, the R-squared score on the testing data was the highest among our different models. We recommend regulators use our Random Forest model for predicting sea level due to its low RMSE and high R-squared score. 

Random Forest models offer a level of interpretability over say black-box models like the recurrent neural network (RNN) model we trained, in addition to being more cost-effective and simpler in training. We are able to extract our feature importances form our Random Forest model and we found Elevation and Longitude to be the more important features in predicting the sea level in Alaska. In terms of interpretation, this makes sense in that the innate elevation of each weather station will play a large part in determing the sea level. Sea level is read using tide gauges which have a zero-reference for each given station, or rather a fixed base elevation at a tide station to which all water level measurements are referred. In conjunction with latitude, the geographic location of each tide station played the largest part in mapping its sea level. 

Climate change data was included in our dataset as atmospheric Carbon Dioxide (CO2) Dry Air Mole fractions, recorded by the Barrow Atmospheric Baseline Observatory (BRW) located in Utqiaġvik, Alaska. The readings from the BRW are characterized as 'having an Arctic maritime climate affected by variations of weather and sea ice conditions in the Central Arctic' due to its close proximity to the Arctic Ocean. Despite our presumptions regarding Carbon Dioxide and rising sea level due to its trapping of heat, we found there was almost no correlation between the atmospheric CO2 in BRW and the sea level from our weather stations. Interestingly enough, portions of Alaska have *decreasing* sea levels due to a process called glacial isostatic adjustment. This is the process where even if melting ice sheets in Alaska are contributing to sea level rise across the globe, the volume of ice melt actually leads to a decrease in sea levels off the Alaskan coast. Think of the ice in Alaska's land as a moon with its own gravitational pull.. as the moon itself loses mass, the gravitational pull will be weaker which will then lead to lowered sea levels around Alaska. This may explain why atmospheric CO2 concentration did not play a large part in our models. 

With this in mind, in further studies, it is recommended to make predictions using isolated station data since their location (latitude and elevation) played such a large part in the predictive power of our models. If doing so, it would be recommended to use more frequent data observations such as hourly average when it comes to sea level to increase the overall sample population. Future studies should account for the glacial isostatic adjustment in Alaska which makes it such a unique area to study in regards to sea level rise. We would also recommend recording new station data around the Alaskan coast. There was a lack of historical data from coastlines in the northeast and northern regions of Alaska, with which if more station points were available, could only improve future models by having a wealth of data points tied around different elevations. Finally, incorporating a diverse set of features such as sea surface salinity, sea surface temperature, and mean sea level pressure (2020, Sithara) would further enhance research into this area. 

## Future Considerations:

- Further Data Collection
    - Time Series Modeling using newer techniques learned since working on this Project
- Entirely different region for study (e.g. Florida - the completely opposite end of Alaska)
- Setting up new weather stations (We only have data for 7 weather stations)
- Further features to consider (e.g. Sea surface temperature, sea level pressure, surface salinity, plate tectonic information)

