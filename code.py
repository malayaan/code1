import pandas as pd

# Création d'un DataFrame exemple
data = {
    'Ville': ['Paris', 'Paris', 'Paris', 'Lyon', 'Lyon', 'Lyon'],
    'Quartier': ['Quartier 1', 'Quartier 1', 'Quartier 1', 'Quartier 2', 'Quartier 2', 'Quartier 2'],
    'Rue': ['Rue A', 'Rue A', 'Rue C', 'Rue B', 'Rue B', 'ALL'],
    'Type_incident': ['Feu', 'Inondation', 'Feu', 'Feu', 'Accident', 'Accident']
}
df = pd.DataFrame(data)

# Affichage du DataFrame original
print("DataFrame original:")
print(df)

def determine_type(group):
    # Comme 'group' est une Series, pas besoin de spécifier la colonne par son nom
    if group.nunique() == 1:
        return group.iloc[0]  # Retourne l'unique type d'incident
    else:
        return 'Unknown'  # Retourne 'Unknown' si divers types d'incidents


# Appliquer la logique de détermination de type d'incident et supprimer les doublons
# Appliquer la fonction de détermination de type d'incident
df['Type_incident'] = df.groupby(['Ville', 'Quartier', 'Rue'])['Type_incident'].transform(determine_type)
df = df.drop_duplicates(subset=['Ville', 'Quartier', 'Rue'])

# Affichage du DataFrame après traitement
print("\nDataFrame après traitement des doublons avec condition sur le type d'incident:")
print(df)
