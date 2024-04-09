import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('dfbk.csv')  # Remplacez 'dfbk.csv' par le chemin vers votre fichier

# Nettoyer les données : supprimer les espaces superflus et séparer les métriques
metrics_list = df['ScopeOfData'].str.replace(" ", "").str.split(';')

# Compter les occurrences de chaque métrique
metrics_count = pd.Series([metric for sublist in metrics_list.dropna() for metric in sublist]).value_counts()

# Visualiser les résultats
plt.figure(figsize=(12, 8))
metrics_count.plot(kind='bar')
plt.title('Nombre d\'occurrences par métrique')
plt.xlabel('Métrique')
plt.ylabel('Nombre d\'occurrences')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
