import pandas as pd
import logging
import os

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/validation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

df = pd.read_csv('data/cleaned/dataset_enriched.csv')

if df.isnull().sum().sum() == 0:
    logging.info('No missing values found')
else:
    logging.warning('Missing values detected')

duplicate_count = df.duplicated().sum()
if duplicate_count == 0:
    logging.info('No duplicate rows found')
else:
    logging.warning(f'Duplicate rows found: {duplicate_count}')

logging.info(f'Total rows: {len(df)}')
print('Validation complete!')