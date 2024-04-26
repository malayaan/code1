import pandas as pd
from itertools import combinations

# ... [autre code] ...

# Calculer le nombre total de combinaisons possibles
total_combinations = len(list(combinations(unique_product_types, 2)))

# Initialiser un compteur d'itérations
count = 0

# Remplir la matrice de co-occurrence
for context, group in df_clean.groupby('context'):
    product_types = group['Product Type'].tolist()
    
    # Créer toutes les paires possibles
    for (product_type_1, product_type_2) in combinations(product_types, 2):
        co_occurrence_matrix.at[product_type_1, product_type_2] += 1
        co_occurrence_matrix.at[product_type_2, product_type_1] += 1  # La matrice est symétrique
        
        # Mettre à jour le compteur d'itérations
        count += 1
        
        # Calculer le pourcentage restant
        percentage_done = (count / total_combinations) * 100
        print(f"Progression : {percentage_done:.2f}%", end='\r')  # Utiliser 'end='\r'' pour écraser la ligne précédente

# Afficher la matrice de co-occurrence
print(co_occurrence_matrix)
