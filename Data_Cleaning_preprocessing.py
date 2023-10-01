"""
Vinayak Vyas ID- 10392
Data-Science Internship Main-Flow Task1 
Data Cleaning and Preprocessing
""" 

import pandas as pd
import numpy as np

# Task1: Identify and handle missing data
# To identify Null values and replace them with Mode for non-numeric columns and with Mean for numeric columns

data = pd.read_csv(r"C:\Users\vinay\Downloads\01.Data Cleaning and Preprocessing.csv")

print("Before Processing")
print(data)

for column_name in data.columns:
    if pd.api.types.is_numeric_dtype(data[column_name]):
        # For numeric columns, fill missing values with the mean
        mean_value = data[column_name].mean()
        data[column_name].fillna(mean_value, inplace=True)
    else:
        # For non-numeric columns, fill missing values with the mode
        mode_value = data[column_name].mode().iloc[0]
        data[column_name].fillna(mode_value, inplace=True)       

# Task2: Remove duplicates

data.drop_duplicates(inplace=True)

# Task3: Detect and handle outliers and perform scaling for numeric columns

def calculate_z_score(dataset):
    mean = np.mean(dataset)
    std_dev = np.std(dataset)
    z_scores = [(x - mean) / std_dev for x in dataset]
    return z_scores

def handle_outliers(dataset, threshold=2):
    z_scores = calculate_z_score(dataset)
    mean_value = np.mean(dataset)
    outliers = []  # Initialize an empty list to store outliers
    for i, z in enumerate(z_scores):
        if abs(z) > threshold:
            outliers.append((i, dataset[i]))  # Store the index and value of the outlier
            dataset[i] = mean_value
    return dataset, outliers

if __name__ == "__main__":
    # threshold for identifying outliers
    threshold = 2
    
    # Separate numeric and non-numeric columns
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    non_numeric_columns = data.select_dtypes(exclude=[np.number]).columns
    
    # Handle outliers and scaling for numeric columns
    for column_name in numeric_columns:
        data_column = data[column_name].tolist()
        
        # Handling outliers and getting the outliers
        data_column, detected_outliers = handle_outliers(data_column, threshold)
        
        # Manually scale the data to have zero mean and unit variance
        mean_value = np.mean(data_column)
        std_dev = np.std(data_column)
        data[column_name] = [(x - mean_value) / std_dev for x in data_column]
    
    
    # saving the cleaned data to a CSV file
    print("After processing")
    print(data)
    data.to_csv(r"C:\Users\vinay\Downloads\01.Data Cleaning and Preprocessing_cleaned.csv", index=False)
