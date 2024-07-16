import pandas as pd

# Exemple de création des DataFrames
df_train = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'other_info': [1, 2, 3]
})

df_test = pd.DataFrame({
    'name': ['Alice', 'Dave', 'Eve']
})

df_dico = pd.DataFrame({
    'name': ['Alice', 'Charlie', 'Eve', 'Luc'],
    'emb1': [0.1, 0.2, 0.3, 2],
    'emb2': [0.4, 0.5, 0.6, 5],
    'emb3': [0.7, 0.8, 0.9, 8]
})

# Filtrer df_dico pour ne conserver que les noms présents dans df_train ou df_test
names_in_use = pd.concat([df_train['name'], df_test['name']]).unique()
df_dico_filtered = df_dico[df_dico['name'].isin(names_in_use)]

# Fusion des DataFrames avec df_dico filtré
df_train = df_train.merge(df_dico_filtered, on='name', how='left')
df_test = df_test.merge(df_dico_filtered, on='name', how='left')

# Calcul de l'embedding médian pour df_train
median_emb = df_train[['emb1', 'emb2', 'emb3']].median()

# Remplacement des NaN par l'embedding médian dans df_train et df_test
df_train[['emb1', 'emb2', 'emb3']] = df_train[['emb1', 'emb2', 'emb3']].fillna(median_emb)
df_test[['emb1', 'emb2', 'emb3']] = df_test[['emb1', 'emb2', 'emb3']].fillna(median_emb)

# Affichage des résultats
print("DataFrame Train après traitement des NaN:")
print(df_train)
print("\nDataFrame Test après traitement des NaN:")
print(df_test)
