"""

Pour commencer ton exploration sur Python et la visualisation de données, nous allons charger l'historique des cours boursiers pour la Société Générale sur une période d'un an, puis utiliser la bibliothèque Matplotlib pour visualiser ces données. Voici les étapes à suivre :
"""
### 1. Installation des bibliothèques nécessaires
"""
Assure-toi d'avoir Python installé sur ton ordinateur. Ensuite, tu auras besoin de quelques bibliothèques, notamment `pandas` pour gérer les données, `matplotlib` pour la visualisation, et `yfinance` pour récupérer les données boursières. Tu peux les installer avec la commande suivante :
"""
pip install pandas matplotlib yfinance

### 2. Charger les données historiques de la bourse
"""
Nous allons utiliser la bibliothèque `yfinance` pour télécharger les données historiques. Voici un script de base pour charger les données de la Société Générale (symbole boursier : "GLE.PA") pour la dernière année :

"""
import yfinance as yf
import pandas as pd

# Définir le symbole boursier
ticker_symbol = "GLE.PA"

# Charger les données
data = yf.download(ticker_symbol, start="2023-01-01", end="2023-12-31")

# Afficher les premières lignes de données
print(data.head())


### 3. Visualiser les données avec Matplotlib
"""
Une fois que tu as les données, tu peux commencer à les visualiser. Voici un exemple de code pour tracer le cours de clôture de l'action au fil du temps :

"""
import matplotlib.pyplot as plt

# Tracer le cours de clôture
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Cours de clôture')
plt.title('Cours de clôture de la Société Générale en 2023')
plt.xlabel('Date')
plt.ylabel('Prix de clôture (€)')
plt.legend()
plt.grid(True)
plt.show()
```

### 4. Paramétrer l'affichage avec Matplotlib
"""
Pour rendre le graphique plus informatif, tu peux ajouter des paramètres supplémentaires :

- **Changer les couleurs et le style de ligne** : `plt.plot(data['Close'], color='red', linestyle='--')`
- **Ajouter des annotations** : `plt.text(specific_date, price, 'Annotation')`
- **Configurer les axes** : `plt.xlim([start_date, end_date])` et `plt.ylim([min_price, max_price])`

Chaque étape te permet de personnaliser davantage ton graphique selon tes besoins spécifiques.
"""
### 5. Expérimenter et explorer
"""
Une fois que tu maîtrises les bases, essaie de tracer d'autres types de données comme les prix d'ouverture, les hauts et les bas journaliers, ou même calculer des moyennes mobiles. Expérimente avec différentes configurations pour mieux comprendre les données.

Ce projet te donnera une bonne introduction à Python pour la manipulation et la visualisation de données. Amuse-toi bien avec ces outils et explore les différentes possibilités qu'ils offrent !
"""