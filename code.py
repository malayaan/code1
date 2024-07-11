import pandas as pd

# Simulation des données d'entraînement et de test
data_train = {
    'underlyingtype': ['Equity', 'Bond', 'Equity', 'Bond', 'Equity', 'Bond'],
    'producttype': ['Option', 'Future', 'Option', 'Future', 'Option', 'Future'],
    'type': ['Incident', 'No Incident', 'No Incident', 'Incident', 'Incident', 'No Incident']
}
data_test = {
    'underlyingtype': ['Equity', 'Bond', 'Equity', 'Bond'],
    'producttype': ['Option', 'Future', 'Option', 'Future'],
    'type': ['Incident', 'Incident', 'No Incident', 'No Incident']
}

X_train = pd.DataFrame(data_train)
y_train = X_train.pop('type')  # Si 'type' est la cible, nous devons l'encoder numériquement pour le mean encoding
X_test = pd.DataFrame(data_test)
y_test = X_test.pop('type')

# Mapping des types d'incidents en valeurs numériques pour y_train
type_mapping = {'Incident': 1, 'No Incident': 0}
y_train = y_train.map(type_mapping)
y_test = y_test.map(type_mapping)

# Calcul du mean encoding pour 'underlyingtype' et 'producttype' en utilisant y_train
mean_encode_underlying = X_train.groupby('underlyingtype')['type'].mean()
mean_encode_product = X_train.groupby('producttype')['type'].mean()

# Appliquer le mean encoding sur X_train et X_test
X_train['underlyingtype_encoded'] = X_train['underlyingtype'].map(mean_encode_underlying)
X_train['producttype_encoded'] = X_train['producttype'].map(mean_encode_product)

X_test['underlyingtype_encoded'] = X_test['underlyingtype'].map(mean_encode_underlying)
X_test['producttype_encoded'] = X_test['producttype'].map(mean_encode_product)

# Affichage des DataFrames après l'encodage
print("X_train with mean encoding:")
print(X_train)
print("\nX_test with mean encoding:")
print(X_test)
