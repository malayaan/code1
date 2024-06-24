import pandas as pd

# Données initiales
data = {
    'product_name': ['prod1', 'prod2', 'prod3', 'prod1', 'prod2'],
    'product_type': ['type1', 'type1', 'type2', 'type2', 'type3'],
    'perimetre': ['perim1', 'perim1', 'perim2', 'perim3', 'perim1']
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# Matrice d'incidence pour product_type
incidence_type = pd.crosstab(df['product_name'], df['product_type'])

# Matrice d'incidence pour perimetre
incidence_perimetre = pd.crosstab(df['product_name'], df['perimetre'])

# Calcul des matrices de cooccurrence
cooccurrence_type = incidence_type.dot(incidence_type.T)
cooccurrence_perimetre = incidence_perimetre.dot(incidence_perimetre.T)

# Addition des deux matrices de cooccurrence
cooccurrence_combined = cooccurrence_type + cooccurrence_perimetre

# Affichage de la matrice combinée
print(cooccurrence_combined)
