# ISDN3000C Lab 05: Plant Sensor Data Analysis

## Project Overview

This project is a comprehensive data analysis assignment for ISDN3000C that focuses on working with plant sensor data using Python's scientific computing libraries: NumPy, Pandas, and Matplotlib. The project involves generating synthetic sensor data from a smart plant monitoring system and performing various data analysis tasks.

## Project Structure

```
ISDN3000C_Lab05/
├── readme.md                 # This file
├── requirements.txt          # Python dependencies
├── getting_started.py        # Data generation script
├── plant_sensors.csv         # Generated sensor data
├── part1.py                  # NumPy exercises
├── part2.py                  # Pandas exercises  
├── part3.py                  # Matplotlib exercises
├── final_challenge.ipynb     # Jupyter notebook with advanced visualizations
├── questions.md              # Answer sheet for lab questions
├── output.png                # Generated visualization output
└── .gitignore               # Git ignore file
```

## Dataset Description

The project uses a synthetic dataset (`plant_sensors.csv`) containing sensor readings from a smart plant monitoring system with the following features:

- **5 sensors** monitoring different plants across 3 locations
- **Hourly readings** for the entire month of July 2023 (3,605 total records)
- **Sensor locations**: Living Room, Office, and Patio
- **Plant types**: Fiddle Leaf Fig, Monstera, Snake Plant, Pothos, and Tomato

### Data Fields

- `timestamp`: Date and time of reading (YYYY-MM-DD HH:MM:SS)
- `sensor_id`: Sensor identifier (A-1, A-2, B-1, B-2, C-1)
- `plant_type`: Type of plant being monitored
- `location`: Physical location of the sensor
- `temperature_c`: Temperature in Celsius
- `soil_moisture`: Soil moisture percentage
- `light_level`: Light level in lux
- `pump_active`: Binary indicator for automatic watering system activation

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Dependencies

- `notebook==7.4.7` - Jupyter notebook environment
- `pandas==2.3.3` - Data manipulation and analysis
- `numpy==2.3.3` - Numerical computing
- `matplotlib==3.10.6` - Data visualization

## Lab Exercises

### Part 1: NumPy Basics (`part1.py`)

Focuses on fundamental NumPy operations including:
- Array creation and manipulation
- Statistical calculations (mean, median, quartiles, standard deviation)
- Boolean indexing and logical operations
- Data calibration and filtering

Key learning outcomes:
- Loading data with `np.genfromtxt()`
- Handling missing values with NaN-aware functions
- Creating boolean masks for data filtering
- Using `np.where()` for conditional operations

### Part 2: Pandas Data Analysis (`part2.py`)

Covers essential Pandas operations including:
- Data loading and inspection with `pd.read_csv()`
- Data type conversion and datetime handling
- Missing data detection and interpolation
- Data filtering and grouping operations
- Temperature unit conversion (Celsius to Fahrenheit)

Key learning outcomes:
- Converting strings to datetime objects
- Handling missing data with interpolation methods
- Grouping data by categories and calculating aggregations
- Filtering data based on multiple conditions

### Part 3: Matplotlib Visualization (`part3.py`)

Introduces data visualization techniques including:
- Bar charts for categorical comparisons
- Line plots for time series analysis
- Histograms for distribution analysis
- Scatter plots for relationship exploration
- Subplot creation for multiple visualizations

Key learning outcomes:
- Creating different types of plots
- Customizing plot appearance (titles, labels, colors)
- Working with subplots for complex visualizations
- Identifying patterns and anomalies in data

### Final Challenge (`final_challenge.ipynb`)

An advanced Jupyter notebook that combines all learned concepts:
- Interactive data exploration
- Advanced visualization techniques
- Multi-sensor data comparison
- Pattern recognition and analysis

## Key Findings

Based on the analysis performed in the project:

1. **Data Volume**: 3,605 sensor readings generated over 31 days (July 2023)
2. **Temperature Range**: Readings vary throughout the day following natural patterns
3. **Soil Moisture Patterns**: Shows correlation with temperature and light levels
4. **Sensor Performance**: Sensor B-2 operates in the driest environment (39.09% average moisture)
5. **Plant Water Requirements**: Monstera plants require the most frequent watering (249 pump activations)

## Data Quality Considerations

The synthetic dataset includes realistic imperfections:
- **Missing values**: 2% chance of NaN readings to simulate sensor failures
- **Data corruption**: 0.5% chance of complete record corruption
- **Sensor faults**: Sensor B-1 has a 10% chance of producing erroneous high readings
- **Environmental noise**: Random variations added to simulate real-world conditions

## Usage Instructions

1. **Generate the dataset**:
   ```bash
   python getting_started.py
   ```

2. **Run individual exercises**:
   ```bash
   python part1.py  # NumPy exercises
   python part2.py  # Pandas exercises
   python part3.py  # Matplotlib exercises
   ```

3. **Open the Jupyter notebook**:
   ```bash
   jupyter notebook final_challenge.ipynb
   ```
