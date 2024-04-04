import pandas as pd
import matplotlib.pyplot as plt

# Chargement du fichier CSV
df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Liste des colonnes à analyser
colonnes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Configuration de base pour les graphiques
plt.figure(figsize=(10, 6 * len(colonnes)))

for i, col in enumerate(colonnes, 1):
    plt.subplot(len(colonnes), 1, i)
    frequences = df[col].value_counts()
    
    # Pour limiter le nombre d'items affichés, vous pouvez utiliser frequences.head(n)
    frequences.plot(kind='bar', color='skyblue')
    
    plt.title(f'Fréquences des items dans la colonne {col}')
    plt.ylabel('Fréquence')
    plt.xlabel('Item')

# Ajustement des graphiques pour éviter le chevauchement
plt.tight_layout()
plt.show()
