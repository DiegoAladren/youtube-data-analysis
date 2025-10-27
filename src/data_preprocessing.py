import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings to view all columns
pd.set_option('display.max_columns', None)

# Seaborn aesthetic configuration
sns.set(style='whitegrid')

# Absolute path of the project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "USvideos.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Show the first lines
print(df.head())