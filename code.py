import pandas as pd
from itertools import combinations

# ... [autre code] ...

# Calculer le nombre total de combinaisons pour un groupe donné
total_combinations_per_group = len(list(combinations(unique_product_types, 2)))

# Calculer le nombre total de groupes
total_groups = df_clean['context'].nunique()

# Le nombre total de combinaisons est le nombre de groupes multiplié par le nombre de combinaisons par groupe
total_combinations = total_groups * total_combinations_per_group

# Initialiser un compteur d'itérations
count = 0

# Remplir la matrice de co-occurrence
for context, group in df_clean.groupby('context'):
    product_types = group['Product Type'].tolist()
    # Il faut recalculer les combinaisons pour chaque groupe car le nombre de types de produits peut varier
    group_combinations = list(combinations(product_types, 2))
    
    for (product_type_1, product_type_2) in group_combinations:
        co_occurrence_matrix.at[product_type_1, product_type_2] += 1
        co_occurrence_matrix.at[product_type_2, product_type_1] += 1  # La matrice est symétrique
        
        # Mettre à jour le compteur d'itérations
        count += 1

        # Calculer le pourcentage restant
        percentage_done = (count / total_combinations) * 100
        print(f"Progression : {percentage_done:.2f}%", end='\r')

# Afficher la matrice de co-occurrence
print("\n")  # S'assurer de passer à la ligne après la fin de la progression
print(co_occurrence_matrix)
