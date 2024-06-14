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

# Fonction pour déterminer si tous les types d'incidents sont les même
def determine_type(group):
    if group['Type_incident'].nunique() == 1:
        return group['Type_incident'].iloc[0]  # Retourner le type d'incident commun
    else:
        return 'Unknown'  # Retourner 'Unknown' si divers types d'incidents

# Appliquer la logique de détermination de type d'incident et supprimer les doublons
df['Type_incident'] = df.groupby(['Ville', 'Quartier', 'Rue'])['Type_incident'].transform(determine_type)
df = df.drop_duplicates(subset=['Ville', 'Quartier', 'Rue'])

# Affichage du DataFrame après traitement
print("\nDataFrame après traitement des doublons avec condition sur le type d'incident:")
print(df)
