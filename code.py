import pandas as pd

# Exemple de deux DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

df2 = pd.DataFrame({
    'A': [3, 4, 5, 6],
    'B': ['c', 'd', 'e', 'f']
})

# Fusionner les deux DataFrames avec un indicateur
merged_df = df1.merge(df2, on=['A', 'B'], how='outer', indicator=True)

# Séparer les lignes uniques à chaque DataFrame
unique_to_df1 = merged_df[merged_df['_merge'] == 'left_only']
unique_to_df2 = merged_df[merged_df['_merge'] == 'right_only']

print("Lignes uniques à df1:")
print(unique_to_df1)

print("\nLignes uniques à df2:")
print(unique_to_df2)
