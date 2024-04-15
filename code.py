import pandas as pd
import ast
from collections import Counter

# Charger le fichier CSV
df = pd.read_csv('chemin_du_fichier.csv')

# Fonction pour convertir la string formatée en liste
def convert_string_to_list(string):
    try:
        return ast.literal_eval(string)
    except ValueError:
        return []

# Appliquer la fonction à la colonne 'Rowgroup'
df['Rowgroup'] = df['Rowgroup'].apply(convert_string_to_list)

# Extraire toutes les colonnes utilisées dans une liste unique
all_columns_used = [column for sublist in df['Rowgroup'] for column in sublist]

# Utiliser Counter pour compter les occurrences de chaque colonne
column_usage_counts = Counter(all_columns_used)

# Afficher les colonnes les plus fréquentes et leurs comptes
for column, count in column_usage_counts.most_common():
    print(f'Colonne: {column}, Occurrences: {count}')

# Afficher également les statistiques générales
print(f'Total de colonnes uniques utilisées: {len(column_usage_counts)}')
