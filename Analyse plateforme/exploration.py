import pandas as pd

# 1. Charger les données CSV
df = pd.read_csv("Desktop/insta_innov/Analyse_plateforme/Data/Donnees_nettoyees.csv", sep=";")

# 2. Vérifier le nombre de lignes et de colonnes
print("Dimensions du fichier :", df.shape)

# 3. Afficher les noms des colonnes
print("\nNoms des colonnes :")
print(df.columns.tolist())

# 4. Afficher les cinq premières lignes
print("\nAperçu des données :")
print(df.head())
