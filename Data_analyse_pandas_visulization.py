# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: Improve plot style
sns.set(style="whitegrid")

# Task 1: Load Dataset
try:
    # Load Iris dataset directly from seaborn
    df = sns.load_dataset('iris')
    print("Dataset loaded successfully!")
except Exception as e:
    print("Error loading dataset:", e)


# Tasl 2: Basic Data Analysis

# Display first few rows
print("First 5 rows of the dataset:")
display(df.head())

# Explore structure
print("\nDataset info:")
df.info()

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values (if any)
df_cleaned = df.dropna()  # or you could use df.fillna(value) for imputation
print("\nShape after cleaning:", df_cleaned.shape)
# Basic statistics for numerical columns
print("\nStatistical summary:")
display(df_cleaned.describe())

# Group by a categorical column ('species') and compute mean of numerical columns
print("\nMean values grouped by species:")
grouped = df_cleaned.groupby('species').mean()
display(grouped)

# Task 3: Data Visualization
print("\nObservations:")
print("- Setosa tends to have smaller petal lengths and widths.")
print("- Virginica has the largest sepal and petal sizes.")
# 1️⃣ Line chart (trends over dataset index, just as an example)
plt.figure(figsize=(8,5))
plt.plot(df_cleaned.index, df_cleaned['sepal_length'], label='Sepal Length', color='blue')
plt.plot(df_cleaned.index, df_cleaned['sepal_width'], label='Sepal Width', color='red')
plt.title('Sepal Length and Width over Sample Index')
plt.xlabel('Sample Index')
plt.ylabel('Measurement (cm)')
plt.legend()
plt.show()

# 2️⃣ Bar chart (average petal length per species)
plt.figure(figsize=(6,5))
sns.barplot(x='species', y='petal_length', data=df_cleaned, palette='viridis')
plt.title('Average Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3️⃣ Histogram (distribution of sepal length)
plt.figure(figsize=(6,5))
plt.hist(df_cleaned['sepal_length'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4️⃣ Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6,5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df_cleaned, palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()
