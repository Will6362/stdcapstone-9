import pandas as pd

df = pd.read_csv('Data/Cleaned/dataset_enriched.csv')

df.to_csv('Data/Cleaned/dataset_final.csv', index=False)

print("Final dataset saved!")
