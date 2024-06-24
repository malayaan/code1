import pandas as pd
import numpy as np

# Nombre de données
n_data = 1000

# Génération de données fictives
np.random.seed(42)
data = {
    'product_name': np.random.choice(['prod1', 'prod2', 'prod3', 'prod4', 'prod5'], n_data),
    'product_type': np.random.choice(['type1', 'type2', 'type3'], n_data),
    'perimetre': np.random.choice(['perim1', 'perim2', 'perim3'], n_data)
}

df = pd.DataFrame(data)

# Liste unique de tous les product_name
unique_products = df['product_name'].unique()

# Taille de chaque lot
batch_size = 100

# Fonction pour traiter chaque lot
def process_batch(sub_df, all_products):
    incidence_type = pd.crosstab(sub_df['product_name'], sub_df['product_type'])
    incidence_perimetre = pd.crosstab(sub_df['product_name'], sub_df['perimetre'])

    # Assure que toutes les matrices ont les mêmes indices et colonnes
    incidence_type = incidence_type.reindex(index=all_products, columns=all_products, fill_value=0)
    incidence_perimetre = incidence_perimetre.reindex(index=all_products, columns=all_products, fill_value=0)

    cooccurrence_type = incidence_type.dot(incidence_type.T).reindex(index=all_products, columns=all_products, fill_value=0)
    cooccurrence_perimetre = incidence_perimetre.dot(incidence_perimetre.T).reindex(index=all_products, columns=all_products, fill_value=0)

    return cooccurrence_type + cooccurrence_perimetre

# Traitement par lots
results = []
for start in range(0, n_data, batch_size):
    end = start + batch_size
    batch_df = df[start:end]
    result = process_batch(batch_df, unique_products)
    results.append(result)
    # Calcul et affichage de la progression
    progress = (start + batch_size) * 100 / n_data
    print(f"Progress: {progress:.2f}% completed")

# Fusion des résultats
final_result = pd.DataFrame(0, index=unique_products, columns=unique_products)
for matrix in results:
    final_result += matrix

# Affichage de la matrice finale de cooccurrence
print(final_result)
