import pandas as pd

# read file
df = pd.read_csv('Data/raw/dataset.csv')

# remove empty rows
df = df.dropna()

# remove duplicates
df = df.drop_duplicates()

# fix column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# fix date format
df['date'] = pd.to_datetime(df['date'])

# save cleaned file
df.to_csv('Data/Cleaned/dataset_cleaned.csv', index=False)

print("Cleaning complete!")
# add new column: year
df['year'] = df['date'].dt.year

# add new column: month
df['month'] = df['date'].dt.month
