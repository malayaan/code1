import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Exemple de DataFrame
data = {
    'product_name': ['prod1', 'prod2', 'prod3', 'prod1', 'prod2'],
    'product_type': ['type1', 'type1', 'type2', 'type2', 'type3'],
    'perimetre': ['perim1', 'perim1', 'perim2', 'perim3', 'perim1']
}
df = pd.DataFrame(data)

# Compter les cooccurrences pour chaque product_type et perimetre
def get_cooccurrence_matrix(df, col):
    df['count'] = 1
    # Utilisation de crosstab pour créer une matrice produit par produit pour chaque groupe
    co_occurrence = df.pivot_table(index='product_name', columns='product_name', 
                                   values='count', aggfunc='sum', fill_value=0)
    # Assurez-vous que la diagonale est à zéro pour ne pas compter les produits avec eux-mêmes
    np.fill_diagonal(co_occurrence.values, 0)
    return co_occurrence

# Poids pour product_type
type_co_occurrence = df.groupby('product_type').apply(lambda x: get_cooccurrence_matrix(x, 'product_type')).sum(level=0)

# Poids pour perimetre, pondéré double
perim_co_occurrence = df.groupby('perimetre').apply(lambda x: get_cooccurrence_matrix(x, 'perimetre') * 2).sum(level=0)

# Somme pondérée des deux matrices
weighted_co_occurrence = type_co_occurrence + perim_co_occurrence

print("Matrice de cooccurrence pondérée :")
print(weighted_co_occurrence)
