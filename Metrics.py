import numpy as np
import pandas as pd
from scipy import stats

# Sample data
data = [15, 20, 35, 40, 50, 60, 70, 80, 90, 100]

# Convert the data to a numpy array for easier calculations
data_array = np.array(data)

# Mean
mean = np.mean(data_array)

# Median
median = np.median(data_array)

# Mode
mode = stats.mode(data_array).mode[0]  # mode returns a ModeResult object

# Percentiles (25th and 75th percentiles)
percentile_25 = np.percentile(data_array, 25)
percentile_75 = np.percentile(data_array, 75)

# Quartiles
first_quartile = np.percentile(data_array, 25)
third_quartile = np.percentile(data_array, 75)

# Range
data_range = np.max(data_array) - np.min(data_array)

# Interquartile Range (IQR)
iqr = third_quartile - first_quartile

# Standard Deviation (SD)
std_dev = np.std(data_array, ddof=0)  # Population SD

# Variance
variance = np.var(data_array, ddof=0)  # Population Variance

# Coefficient of Variation (CV)
coefficient_of_variation = (std_dev / mean) * 100  # CV in percentage

# Displaying the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"25th Percentile: {percentile_25}")
print(f"75th Percentile: {percentile_75}")
print(f"First Quartile (Q1): {first_quartile}")
print(f"Third Quartile (Q3): {third_quartile}")
print(f"Range: {data_range}")
print(f"IQR: {iqr}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Coefficient of Variation: {coefficient_of_variation:.2f}%")