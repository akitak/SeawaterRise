import streamlit as st
import pickle
import numpy as np


st.title('Predicting rise in sea level in Alaska')


page = st.sidebar.selectbox(
'Select a Page',('Home','About','More research','Make a prediction!')
)

if page == 'Home':
    st.write(" Add more here")

if page == 'About':
    st.write(" Add something here")

if page == 'More research':
    st.write(" Add outside research here, Eddie can help u in this.")

if page == 'Make a prediction!':
    features = ['LONGITUDE', 'ELEVATION','TMIN', 'TMAX','PRCP','TAVG']
    st.write('Enter the Longitude:')
    LONGITUDE = st.text_input(label = 'Choose from these 7 places: {Dutch Harbor : -166.5433, Nome Airport : -165.44, Kodiak Airport : -152.4855, Seward Airport : -149.41677, Yakutat Airport : -139.6712, Sitka Airport:  -135.3647, Ketchikan Airport : -131.72074}',value = 0, key = '1')

    st.write('Enter the Elevation:')
    ELEVATION = st.text_input(label = 'Choose from these 7 places: {Dutch Harbor : 3.0, Nome Airport : 4.0, Kodiak Airport : 24.4, Seward Airport : 6.7, Yakutat Airport : 10.1, Sitka Airport:  4.3, Ketchikan Airport : 24.4}',  value = 0,key = '2')

    st.write('Enter the minimum temperature:')
    TMIN = st.text_input(label = 'Range from -55 to 30',  value = 0,key = '3')

    st.write('Enter the maximum temperature:')
    TMAX = st.text_input(label = 'Range from -40 to 60',  value = 0,key = '4')

    st.write('Enter the precipitation:')
    PRCP = st.text_input(label = 'Range from 0 to 400',  value = 0,key = '5')

    st.write('Enter the average change in temperature:')
    TAVG = st.text_input(label = 'Range from -40 to 25',  value = 0,key = '6')

    #For this portion I took help from project 4's streamlit app
    click = st.button('Predict')
    if click:
        with open('Random_Forest_model.pkl', mode = 'rb') as pickle_in:
            pipe = pickle.load(pickle_in)
            input_val = [LONGITUDE, ELEVATION,TMIN, TMAX,PRCP,TAVG]
            input_val = np.reshape(input_val,(1,-1))
            predict = pipe.predict(input_val)

            st.write(f'Prediction: The sea level will be around {predict[0]}')
