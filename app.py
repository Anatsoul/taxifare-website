import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# ''

# '''
title_date = st.date_input('date')
title_time = st.time_input('time')


#st.write('date and time', title_date_time)
title_pickup_longitude = st.number_input('pickup longitude',-73.950655)
#st.write('pickup longitude', title_pickup_longitude)
title_pickup_latitude = st.number_input('pickup latitude',40.783282)
#st.write('pickup latitude', title_pickup_latitude)
title_dropoff_longitude = st.number_input('dropoff longitude',-73.984365)
#st.write('dropoff longitude', title_dropoff_longitude)
title_dropoff_latitude = st.number_input('dropoff latitude',40.769802)
#st.write('dropoff latitude', title_dropoff_latitude)
title_passenger_count = st.text_input('passenger count',2)
#st.write('passenger count', title_passenger_count)

## Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

#🤔 How could we call our API ? Off course... The `requests` package 💡


#url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

   # st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


#2. Let's build a dictionary containing the parameters for our API...

params={'pickup_datetime':f'{title_date} {title_time}',
            'pickup_longitude':title_pickup_longitude,
            'pickup_latitude':title_pickup_latitude,
            'dropoff_longitude':title_dropoff_longitude,
            'dropoff_latitude':title_dropoff_latitude,
            'passenger_count':title_passenger_count}

# @st.cache
# def get_map_data():

#     return pd.DataFrame(
#                         (
#                             (title_pickup_longitude, title_pickup_latitude),(title_dropoff_longitude,title_dropoff_latitude)
#                             )
#             columns=['lat', 'lon'])

# df = get_map_data()
# st.map(df)

#https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longi[…]e=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

#3. Let's call our API using the `requests` package...

url='https://taxifare.lewagon.ai/predict'
response = requests.get(url,params=params).json()
#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user

response['fare']
