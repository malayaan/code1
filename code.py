import pandas as pd

# Données initiales
data = {
    'product_name': ['prod1', 'prod2', 'prod3', 'prod1', 'prod2'],
    'product_type': ['type1', 'type1', 'type2', 'type2', 'type3'],
    'perimetre': ['perim1', 'perim1', 'perim2', 'perim3', 'perim1']
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# Création de la matrice d'incidence entre product_name et product_type
incidence_matrix = pd.crosstab(df['product_name'], df['product_type'])

# Calcul de la matrice de cooccurrence
cooccurrence_matrix = incidence_matrix.dot(incidence_matrix.T)

# Les valeurs sur la diagonale seront le nombre de product_types uniques que chaque product_name apparaît
print(cooccurrence_matrix)
