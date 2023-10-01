"""
Vinayak Vyas ID- 10392
Data-Science Internship Main-Flow Task2 
Exploratery Data Analysis
""" 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_dataset.csv' with the actual dataset path)
df = pd.read_csv(r'C:\Users\vinay\Downloads\INDIAvi.csv')

# Task 1: Generate summary statistics
summary_stats = df.describe()
print(summary_stats)

# Task 2: Visualize data distributions for numerical columns

# Identify numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Loop through each numerical column and create histograms
for column in numerical_columns:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Loop through each numerical column and create box plots
for column in numerical_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, y=column)
    plt.title(f'Box Plot of {column}')
    plt.ylabel('Value')
    plt.show()

# Create scatter plots for all pairs of numerical columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.xlabel(numerical_columns[i])
        plt.ylabel(numerical_columns[j])
        plt.show()

#task3 : Identify correlations and relationships between variables.
correlation_matrix = df[numerical_columns].corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

#task4 : Hypotheses for further analysis
# Hypothesis 1: There is a positive correlation between numerical_column1 and numerical_column2.
# Hypothesis 2: The distribution of values in numerical_column follows a normal distribution.
# Hypothesis 3: There are outliers in numerical_column based on the box plot.
# Hypothesis 4: There is a significant difference in the mean of numerical_column between categories in categorical_column.
# Hypothesis 5: There is a relationship between numerical_column1 and numerical_column2 that varies across different values of categorical_column.
# Hypothesis 6: Some numerical columns are highly correlated with each other, suggesting multicollinearity.
# Hypothesis 7: There may be clusters or patterns in the scatter plots between numerical variables.



