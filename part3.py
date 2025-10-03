# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


'''
Load the datasets
'''
df = pd.read_csv('plant_sensors.csv')


'''
Exercise 3.1: Bar Chart
'''
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['temperature_f'] = df['temperature_c'] * 9/5 + 32
df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear')
df['timestamp'] = df['timestamp'].interpolate(method='linear')
df['sensor_id'] = df['sensor_id'].fillna('Null')
df['temperature_c'] = df['temperature_c'].interpolate(method='linear')
df['light_level'] = df['light_level'].interpolate(method='linear')
df['temperature_f'] = df['temperature_f'].interpolate(method='linear')
df.groupby(['sensor_id'])['soil_moisture'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Soil Moisture by Sensor')
plt.xlabel('Sensor ID')
plt.xticks(rotation=0)
plt.ylabel('Average Moisture (%)')
plt.show()

'''
Exercise 3.2: Line Plot
'''
df.loc[df['sensor_id'] == 'A-1'].set_index('timestamp')['soil_moisture'].plot(kind='line', color='blue')
plt.title('Moisture Level for Sensor A-1')
plt.xlabel('Timestamp')
plt.ylabel('Soil Moisture (%)')
plt.show()

'''
Exercise 3.3: Subplots and Anomaly Detection
'''
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
axes[0].hist(df['temperature_c'], bins=40, color='skyblue', alpha=0.7)
axes[0].set_title('Distribution of All Temperature Readings')
axes[0].set_xlabel('Temperature (°C)')
axes[0].set_ylabel('Frequency')
axes[0].legend()
axes[1].scatter(df['temperature_c'], df['soil_moisture'], color='orange', alpha=0.1)
axes[1].set_title('Temperature vs. Soil Moisture')
axes[1].set_xlabel('Temperature (°C)')
axes[1].set_ylabel('Soil Moisture (%)')
plt.show()
