import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.title('Predicting rise in sea level in Alaska')


page = st.sidebar.selectbox(
'Select a Page',('Home','Make a prediction!')
)

if page == 'Home':

    image = Image.open('st_images/Alaskan_Coastline.jpg')
    st.image(image)

    st.write(
    "As the effects of Global Warming increase, there is growing"+
    " concern regarding what impact rising sea levels will have on society." +
    " It is our team's mission to predict sea levels based on seemingly" +
    " unrelated metrics in order to more easily monitor rising sea levels."+
    " In order to do so we will process data gathered by a range of instituations"+
    " through a comprehensive collection of advanced machine learning techniques."
    " It is through this process that we hope to draw incites, make conclusions"+
    " and provide recommendations for those realms which are being effected. ")

    st.write("                                                                 "+
    "                                                                 " +
    "                                                                 "
    "                                                                 "
    )
    st.title('Meet Our Team')
    image2 = Image.open('st_images/team.png')
    st.image(image2)

    st.title('More Information')
    st.write("Sea level rise poses a huge threat to coastal habitats: Almost 40% of the U.S. Population lives in high-population density coastal areas where sea level can unleash devastating effects. Sea level is a major part when it comes to flooding, shoreline erosion, and storm surges. Increase in either of these can result in infrastructure damage: roads, bridges, subways, water supply, oil and gas wells, pwer plants, sewage treatment plants, and landfills.")
    st.image('https://www.coastalhazardwheel.org/media/1310/noaa-katrina-new-orleans-flooding3-2005-test2.jpg', caption = 'Coastal flooding devasataion.')

    st.write("Rate of sea level rise has been accelerating: For most of the twentieth century, the rate of sea level rise was around 0.06 inches (1.4 millimeters). It has since more than doubled to a rate of 0.14 inches (3.6 millimeters) a year from 2006 - 2015. The cause? Global warming, or more specifically, the ice and glacier melt caused by rising global mean temperature as well as the ocean volume due to the temperature of water rising. The increase in fossil fuel emissions, deforestation, and agriculture farming. ")
    st.image('https://cdn.britannica.com/67/106467-050-1EF12FB5/concentration-carbon-dioxide-atmosphere-greenhouse-gases-Earth-1750.jpg', caption = 'Greenhouse gas radiative forcings')
    st.title('Relevant Sources')
    st.write("AR6 Climate Change 2021: https://www.ipcc.ch/report/ar6/wg1/#SPM")
    st.write( "NOAA Climate Data Online: https://www.ncdc.noaa.gov/cdo-web/datasets")
    st.write( "NCEI Products: https://www.ncei.noaa.gov/products#air")
    st.write( "PNAS Alaskan CO2 Sources: https://www.pnas.org/content/114/21/5361")
    st.write( "PSMSL Obtaining Sea Level Data: https://www.psmsl.org/data/hf/")
    st.write( "Sea-level rise caused by climate change (implications for society) -Nobuo Mimura: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3758961/")

if page == 'Make a prediction!':
    features = ['LONGITUDE', 'ELEVATION','TMIN', 'TMAX','PRCP','TAVG']
    st.write('Choose a Weather Station:')

    weather_station = st.radio("Please choose from one of these 7 weather station locations:", ('Dutch Harbor', 'Ketchikan','Kodiak', 'Nome', 'Seward','Sitka','Yakutat'))

    if weather_station == 'Dutch Harbor':
        LONGITUDE = -166.5433
        ELEVATION = 3.0

    if weather_station == 'Ketchikan':
        LONGITUDE = -131.72074
        ELEVATION = 3.0

    if weather_station == 'Kodiak':
        LONGITUDE = -152.4855
        ELEVATION = 24.4

    if weather_station == 'Nome':
        LONGITUDE = -165.44
        ELEVATION = 4.0

    if weather_station == 'Seward':
        LONGITUDE = -149.41677
        ELEVATION = 6.7

    if weather_station == 'Sitka':
        LONGITUDE = -135.3647
        ELEVATION = 4.3

    if weather_station == 'Yakutat':
        LONGITUDE = -139.6712
        ELEVATION = 10.1

    st.write('Enter the minimum temperature(C):')
    TMIN = st.text_input(label = 'Range from -55 to 30',  value = 0,key = '3')

    st.write('Enter the maximum temperature(C):')
    TMAX = st.text_input(label = 'Range from -40 to 60',  value = 0,key = '4')

    st.write('Enter the precipitation(mm):')
    PRCP = st.text_input(label = 'Range from 0 to 400',  value = 0,key = '5')

    st.write('Enter the average change in temperature(C):')
    TAVG = st.text_input(label = 'Range from -40 to 25',  value = 0,key = '6')

    #For this portion I took help from project 4's streamlit app
    click = st.button('Predict')
    if click:
        with open('Random_Forest_model.pkl', mode = 'rb') as pickle_in:
            pipe = pickle.load(pickle_in)
            input_val = [LONGITUDE, ELEVATION,TMIN, TMAX,PRCP,TAVG]
            input_val = np.reshape(input_val,(1,-1))
            predict = pipe.predict(input_val)

            st.write(f'Prediction: The sea level will be around {predict[0]}(cm)')
