import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
import utils

# Settings to view all columns
pd.set_option('display.max_columns', None)

# Seaborn aesthetic configuration
sns.set(style='whitegrid')

# Relative path of the project
csv_path = os.path.join("..", "data", "USvideos.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Remove duplicates
df.drop_duplicates()

# Remove critical rows with null values (none should be removed based on what we have seen above).
df = df.dropna(subset=['title', 'channel_title', 'category_id'])

# Converting date columns
df = utils.convert_to_datetime(df, 'trending_date', format='%y.%d.%m')
df = utils.convert_to_datetime(df, 'publish_time')

# Creating auxiliar columns
df['publish_date'] = df['publish_time'].dt.date
df['publish_hour'] = df['publish_time'].dt.hour

# Interaction rate
df = utils.calculate_ratios(df)

# Converting to date
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')

# Splitting tags
df['tags_list'] = df['tags'].str.split('|')

# Load JSON
with open("../data/US_category_id.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create mapping id → title
category_map = {int(item['id']): item['snippet']['title'] for item in data['items']}

# Check
print(category_map)

df = utils.map_category(df, category_map)

# Check
df[['category_id', 'category_name']].head()


clean_csv_path = os.path.join("..", "data", "USvideos_clean.csv")

# save CSV
df.to_csv(clean_csv_path, index=False)

print("Clean dataset saved in:", clean_csv_path)
