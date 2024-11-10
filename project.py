# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset from CSV (replace 'your_file.csv' with the actual path to your file)
df = pd.read_csv('DoctorVisits.csv')

# Display the first few rows to ensure the dataset is loaded correctly
print("Dataset Preview:")
print(df.head())

# Basic descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 1. Distribution of income across the dataset
plt.figure(figsize=(8, 6))
sns.histplot(df['income'], bins=5, kde=True, color='skyblue')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# 2. Gender vs. Income comparison (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='income', data=df, palette='Set2')
plt.title('Income Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Income')
plt.show()

# 3. Illness Severity vs. Reduced Health (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='illness', y='reduced', hue='health', data=df, palette='coolwarm', s=100)
plt.title('Illness Severity vs. Reduced Health')
plt.xlabel('Illness Severity')
plt.ylabel('Reduced Health')
plt.legend(title='Health Condition')
plt.show()

# 4. Private vs. Free Healthcare Access (Pie Chart)
healthcare_access = df['private'].value_counts()
plt.figure(figsize=(6, 6))
healthcare_access.plot.pie(autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
plt.title('Private Healthcare Access vs. Free Healthcare Access')
plt.ylabel('')
plt.show()

# 5. Chronic Conditions and Reduced Health (Bar Plot)
chronic_data = df[df['nchronic'] == 'yes']
plt.figure(figsize=(8, 6))
sns.countplot(x='reduced', data=chronic_data, palette='Blues')
plt.title('Impact of Chronic Conditions on Reduced Health')
plt.xlabel('Reduced Health Severity')
plt.ylabel('Count')
plt.show()

# Correlation Analysis (Optional - Pearson's correlation)
correlation_matrix = df[['income', 'illness', 'reduced']].apply(pd.to_numeric, errors='coerce').corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
