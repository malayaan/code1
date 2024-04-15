import pandas as pd
import matplotlib.pyplot as plt

# Étape 1: Lire le fichier CSV
df = pd.read_csv('chemin_du_fichier.csv')

# Étape 2: Listes des applications
app1 = ['app_a', 'app_b']
app2 = ['app_c', 'app_d']
app3 = ['app_e', 'app_f']
app4 = ['app_g', 'app_h']

# Étape 3: Créer un dictionnaire pour compter les occurrences
counts = {'app1': 0, 'app2': 0, 'app3': 0, 'app4': 0}

# Classer chaque application
for app in df['col1']:
    if app in app1:
        counts['app1'] += 1
    elif app in app2:
        counts['app2'] += 1
    elif app in app3:
        counts['app3'] += 1
    elif app in app4:
        counts['app4'] += 1

# Étape 4: Créer un graphique à barres
plt.bar(counts.keys(), counts.values(), color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Liste des applications')
plt.ylabel('Nombre d\'incidents')
plt.title('Nombre d\'incidents par liste d\'applications')
plt.show()
