import pandas as pd

# Supposons que df1 et df2 sont déjà définis
# Exemple de données:
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

df2 = pd.DataFrame({
    'A': [1, 2, 5, 6],
    'B': ['a', 'b', 'e', 'f']
})

# Utiliser merge avec l'indicateur, cela ajoutera une colonne '_merge' indiquant l'origine de chaque ligne
merged_df = pd.merge(df1, df2, on=['A', 'B'], how='outer', indicator=True)

# Filtrer les lignes qui sont uniques à chaque DataFrame
only_in_df1 = merged_df[merged_df['_merge'] == 'left_only']
only_in_df2 = merged_df[merged_df['_merge'] == 'right_only']

print("Lignes uniquement dans df1:")
print(only_in_df1)

print("Lignes uniquement dans df2:")
print(only_in_df2)
