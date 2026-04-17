import pandas as pd

df = pd.read_csv('Data/Cleaned/dataset_cleaned.csv')

df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 50, 100],
    labels=['Teen', 'Young Adult', 'Adult', 'Senior']
)

df['purchase_category'] = pd.cut(
    df['purchas_amount'],
    bins=[0, 100, 500, 1000, 5000],
    labels=['Low', 'Medium', 'High', 'VIP']
)

df.to_csv('Data/Cleaned/dataset_enriched.csv', index=False)

print("Enrichment complete!")