import pandas as pd
from itertools import combinations
import numpy as np

# ... [autre code] ...

# Initialisation de la matrice de co-occurrence avec numpy
unique_product_types = df_clean['Product Type'].unique()
co_occurrence_matrix_np = np.zeros((len(unique_product_types), len(unique_product_types)))

# Création d'un mappage entre les types de produits et les indices de la matrice
product_type_to_index = {product_type: index for index, product_type in enumerate(unique_product_types)}

# Préparation pour l'indication de progression
total_groups = df_clean['context'].nunique()
group_count = 0

# Remplir la matrice de co-occurrence
for context, group in df_clean.groupby('context'):
    product_types_indices = [product_type_to_index[product_type] for product_type in group['Product Type']]
    for (index1, index2) in combinations(product_types_indices, 2):
        co_occurrence_matrix_np[index1, index2] += 1
        co_occurrence_matrix_np[index2, index1] += 1  # La matrice est symétrique

    # Mise à jour de la progression
    group_count += 1
    percentage_done = (group_count / total_groups) * 100
    print(f"Progression : {percentage_done:.2f}%", end='\r')

# Convertir la matrice numpy en DataFrame pour l'affichage
co_occurrence_matrix = pd.DataFrame(co_occurrence_matrix_np, index=unique_product_types, columns=unique_product_types)

# Afficher la matrice de co-occurrence
print("\nTerminé.")
print(co_occurrence_matrix)
