import pandas as pd
import os

# Obtener la ruta absoluta del proyecto (un nivel arriba de src/)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(base_dir, "data", "USvideos.csv")

df = pd.read_csv(csv_path)

print(df.head(10))
