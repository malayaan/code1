import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le DataFrame
df = pd.read_csv('votre_fichier.csv')

# Inspecter les premières lignes du DataFrame
print("Aperçu des premières lignes du DataFrame :")
print(df.head())

# Comprendre la structure et les types de données
print("\nTypes de données dans le DataFrame :")
print(df.dtypes)

# Analyse descriptive : Calculer les statistiques descriptives pour chaque colonne de type float
print("\nStatistiques descriptives des colonnes de type float :")
print(df.describe())

# Visualisation initiale : Créer des visualisations pour chaque variable
# Histogrammes
for column in df.select_dtypes(include=['float64']).columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f'Histogramme de {column}')
    plt.xlabel(column)
    plt.ylabel('Fréquence')
    plt.show()

# Boxplots
for column in df.select_dtypes(include=['float64']).columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot de {column}')
    plt.xlabel(column)
    plt.show()
