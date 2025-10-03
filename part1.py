import numpy as np
import pandas as pd

# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #

'''
Load the datasets
'''


'''
Exercise 1.1: Array Basics
'''
moisture_readings = np.genfromtxt('plant_sensors.csv', delimiter=',', usecols=[-3], skip_header=1)
calibrated_moisture = moisture_readings + 0.5
print("Calibrated Moisture Readings:" , calibrated_moisture[0:5])

'''
Exercise 1.2: Array Slicing and Stats
'''
print("Moisture Readings Stats:", moisture_readings[50:60])
print("Mean Moisture Reading:", np.nanmean(moisture_readings))
print("Median Moisture Reading:", np.nanmedian(moisture_readings))
print("Quartiles of Moisture Readings:", np.nanpercentile(moisture_readings, [25, 50, 75]))
print("Standard Deviation of Moisture Readings:", np.nanstd(moisture_readings))


'''
Exercise 1.3: Boolean Indexing and Logic
'''
less_than_35_mask = ~np.isnan(moisture_readings) & (moisture_readings < 35)
dry_readings = moisture_readings[less_than_35_mask]
print("Dry Readings (<35):", dry_readings.shape[0])
moisture_status = np.where(moisture_readings < 35, 'Dry', 'OK')
moisture_status = np.where(moisture_readings > 70, 'Wet', moisture_status)
print(moisture_status[1470:1480])