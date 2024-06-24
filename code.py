from sklearn.preprocessing import StandardScaler
import pandas as pd

# Création d'un DataFrame exemple
data = {
    'perimetre': ['zone1', 'zone2', 'zone3', 'zone4'],
    'type': ['type1', 'type2', 'type3', 'type4'],
    'feature1': [20, 21, 19, 18],
    'feature2': [30, 31, 29, 28],
    # Ajoutez ici les autres colonnes nécessaires...
}
df = pd.DataFrame(data)

# Supposons que les colonnes à scaler sont 'feature1' et 'feature2'
columns_to_scale = ['feature1', 'feature2']  # Vous ajouterez ici les noms réels des 13 colonnes

# Initialisation du StandardScaler
scaler = StandardScaler()

# Scaling des colonnes spécifiques
df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

# Vérification des résultats
print(df)
