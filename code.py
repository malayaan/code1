import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Liste des colonnes à analyser
colonnes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Calcul et affichage des fréquences pour chaque colonne
for col in colonnes:
    print(f"Fréquences pour la colonne '{col}':")
    frequences = df[col].value_counts()
    print(frequences)
    print("\n")
