import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Fonction pour compter les occurrences
def compter_occurrences(df, colonne_reference, autres_colonnes):
    resultats = {}
    valeurs_reference = df[colonne_reference].unique()

    for valeur in valeurs_reference:
        comptes = {col: df[col].tolist().count(valeur) for col in autres_colonnes}
        resultats[valeur] = comptes

    return resultats

# Colonnes à comparer
colonne_reference = 'a'
autres_colonnes = ['b', 'c', 'd', 'e', 'f', 'g']

# Appel de la fonction
occurrences = compter_occurrences(df, colonne_reference, autres_colonnes)

# Affichage des résultats
for valeur, comptes in occurrences.items():
    print(f"Valeur '{valeur}' de la colonne '{colonne_reference}' apparaît dans:")
    for col, compte in comptes.items():
        if compte > 0:
            print(f" - {compte} fois dans la colonne '{col}'")
    print("\n")
