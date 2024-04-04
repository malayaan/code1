import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Liste des noms de colonnes à supprimer
colonnes_a_supprimer = ['nom_colonne1', 'nom_colonne2']  # Modifiez ceci selon vos besoins

# Suppression des colonnes
df_modifie = df.drop(columns=colonnes_a_supprimer)

# Enregistrement du DataFrame modifié dans un nouveau fichier CSV
df_modifie.to_csv('chemin/vers/votre/nouveau_fichier.csv', index=False)

print(f"Le fichier a été enregistré avec succès sans les colonnes : {', '.join(colonnes_a_supprimer)}")
