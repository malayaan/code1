import pandas as pd
from tqdm import tqdm

# Création de DataFrame exemple df1
data1 = {
    'strings': ['hello 123', 'world 456', 'test 789', 'example 101']
}
df1 = pd.DataFrame(data1)

# Création de DataFrame exemple df2
data2 = {
    'ints': [123, 789, 654]
}
df2 = pd.DataFrame(data2)

# Convertir les entiers en chaînes
df2['ints_str'] = df2['ints'].astype(str)
pattern = '|'.join(df2['ints_str'].tolist())  # '123|789|654'

# Utiliser str.contains pour filtrer df1
tqdm.pandas(desc="Matching strings")
df1['match'] = df1['strings'].progress_apply(lambda x: bool(re.search(pattern, x)))

# Filtrer pour obtenir les résultats
filtered_df1 = df1[df1['match']]

print(filtered_df1)
