# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import numpy as np
import pandas as pd


'''
Load the datasets
'''
df = pd.read_csv('plant_sensors.csv')


'''
Exercise 2.1: Initial Inspection & Cleaning
'''
print(df.head())
print(df.info())
print(df.shape)
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['temperature_f'] = df['temperature_c'] * 9/5 + 32
print(df['timestamp'].dt.hour)
print(df['temperature_f'])

'''
Exercise 2.2: Missing Data & Filtering
'''
print(df.isnull().sum())
df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear')
df['timestamp'] = df['timestamp'].interpolate(method='linear')
df['sensor_id'] = df['sensor_id'].fillna('Null')
df['temperature_c'] = df['temperature_c'].interpolate(method='linear')
df['light_level'] = df['light_level'].interpolate(method='linear')
df['temperature_f'] = df['temperature_f'].interpolate(method='linear')
patio_high_light = df.loc[(df['light_level'] > 1200) & (df['location'] == 'Patio')]

'''
Exercise 2.3: Grouping and Aggregation
'''
print(df.groupby(['sensor_id'])['soil_moisture'].mean())
print(df.groupby(['plant_type'])['pump_active'].sum())
print(df.loc[df['location'].isin(['Living Room', 'Office', 'Patio'])].groupby(["location"])['temperature_c'].max())
