import pandas as pd
import numpy as np

# Nombre de données
n_data = 4000000

# Génération de données fictives
np.random.seed(42)
data = {
    'product_name': np.random.choice(['prod1', 'prod2', 'prod3', 'prod4', 'prod5'], n_data),
    'product_type': np.random.choice(['type1', 'type2', 'type3'], n_data),
    'perimetre': np.random.choice(['perim1', 'perim2', 'perim3'], n_data)
}

df = pd.DataFrame(data)

# Taille de chaque lot
batch_size = 100000

# Fonction pour traiter chaque lot
def process_batch(sub_df):
    incidence_type = pd.crosstab(sub_df['product_name'], sub_df['product_type'])
    incidence_perimetre = pd.crosstab(sub_df['product_name'], sub_df['perimetre'])
    cooccurrence_type = incidence_type.dot(incidence_type.T)
    cooccurrence_perimetre = incidence_perimetre.dot(incidence_perimetre.T)
    return cooccurrence_type + cooccurrence_perimetre

# Traitement par lots
results = []
for start in range(0, n_data, batch_size):
    end = start + batch_size
    batch_df = df[start:end]
    result = process_batch(batch_df)
    results.append(result)
    # Calcul et affichage de la progression
    progress = (start + batch_size) * 100 / n_data
    print(f"Progress: {progress:.2f}% completed")

# Fusion des résultats
final_result = sum(results)

from sklearn.decomposition import PCA

# Assumons que final_result est correctement calculé et bien aligné
# Conversion du DataFrame final en matrice numpy pour PCA
data_matrix = final_result.values

# Initialisation de PCA pour réduire les dimensions à 3
pca = PCA(n_components=3)

# Ajustement de PCA sur les données et transformation
reduced_data = pca.fit_transform(data_matrix)

# Création d'un nouveau DataFrame à partir des données réduites
reduced_df = pd.DataFrame(reduced_data, columns=['PC1', 'PC2', 'PC3'], index=final_result.index)

# Affichage de la matrice réduite
print("Matrice réduite :")
print(reduced_df)

# (Optionnel) Affichage de la variance expliquée par chaque composante
print("Variance expliquée par chaque composante :")
print

