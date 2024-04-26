import pandas as pd
from itertools import combinations

# Supposons que df est votre DataFrame
# Voici un exemple de données pour illustrer
data = {
    'Product_Type': ['A', 'B', 'A', 'C', 'B', 'D', 'C', 'A'],
    'col1': [1, 1, 2, 2, 3, 3, 3, 1],
    'col2': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'Z', 'X'],
    'col3': ['alpha', 'alpha', 'beta', 'beta', 'gamma', 'gamma', 'gamma', 'alpha']
}
df = pd.DataFrame(data)

# Définir le contexte comme la combinaison de col1, col2 et col3
df['context'] = df[['col1', 'col2', 'col3']].astype(str).agg('_'.join, axis=1)

# Initialiser la matrice de co-occurrence avec des zéros
unique_product_types = df['Product_Type'].unique()
co_occurrence_matrix = pd.DataFrame(0, index=unique_product_types, columns=unique_product_types)

# Remplir la matrice de co-occurrence
for context, group in df.groupby('context'):
    product_types = group['Product_Type'].tolist()
    # Créer toutes les paires possibles dans le contexte
    for (product_type_1, product_type_2) in combinations(product_types, 2):
        co_occurrence_matrix.at[product_type_1, product_type_2] += 1
        co_occurrence_matrix.at[product_type_2, product_type_1] += 1  # La matrice est symétrique

# Afficher la matrice de co-occurrence
print(co_occurrence_matrix)
