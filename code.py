import pandas as pd
import ast

# Charger le fichier CSV
df = pd.read_csv('chemin_du_fichier.csv')

# Fonction pour convertir la string formatée en liste
def convert_string_to_list(string):
    try:
        # Utilise ast.literal_eval pour évaluer en toute sécurité la string comme une expression Python
        return ast.literal_eval(string)
    except ValueError:
        # Retourne une liste vide en cas d'erreur
        return []

# Appliquer la fonction à la colonne 'row groups'
df['row groups'] = df['row groups'].apply(convert_string_to_list)

# Afficher les résultats
print(df)
