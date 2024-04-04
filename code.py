import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Calcul et affichage du nombre de NaN par colonne
nan_par_colonne = df.isna().sum()
print(nan_par_colonne)
