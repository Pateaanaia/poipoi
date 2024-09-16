import pandas as pd

# Charger le fichier Parquet
file_path = '/home/patea/code/Pateaanania/poipoi/resultat_concatenation_avec_date_heure.parquet'
df = pd.read_parquet(file_path)

# Afficher les premières lignes pour vérifier
print(df.head())
