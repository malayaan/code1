# Fusionner toutes les chaînes de df2 en une expression régulière
import re
pattern = '|'.join(df2['ints'].tolist())  # Crée une chaîne comme '123|789|654'

# Filtrer df1 pour les lignes contenant un des motifs
df1['match'] = df1['strings'].apply(lambda x: bool(re.search(pattern, x)))
filtered_df1 = df1[df1['match']]
