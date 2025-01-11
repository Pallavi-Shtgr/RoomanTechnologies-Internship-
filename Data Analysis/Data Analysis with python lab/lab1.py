import pandas as pd

# Create the DataFrame with the provided data for 'Name', 'Age', and 'City'
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, 27, 32, 39, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# 1. Create the 'Age Group' column using pd.cut() with the categories '20s', '30s', '40s'
bins = [20, 29, 39, 49]  # Define the bin ranges for age groups
labels = ['20s', '30s', '40s']  # Labels for the age groups
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True, include_lowest=True)

# 2. Filter the DataFrame to select rows where individuals are in their 30s
filtered_df = df[df['Age Group'] == '30s']

# 3. Calculate and display the mean, median, and variance of the 'Age' column
mean_age = df['Age'].mean()
median_age = df['Age'].median()
variance_age = df['Age'].var()

# Display the DataFrame and results
print("Original DataFrame:")
print(df)

print("\nFiltered DataFrame (Age Group: 30s):")
print(filtered_df)

print("\nStatistics for 'Age' column:")
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Variance of Age: {variance_age}")
