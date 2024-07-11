import pandas as pd

# Supposons que vous avez déjà vos dataframes X_train, X_test, y_train, y_test
# et que 'type' est votre variable cible, jointe avec X_train pour faciliter le groupby
X_train['type'] = y_train

# Calculer le mean encoding pour 'underlyingtype'
mean_underlyingtype = X_train.groupby('underlyingtype')['type'].mean()
X_train['underlyingtype_encoded'] = X_train['underlyingtype'].map(mean_underlyingtype)
X_test['underlyingtype_encoded'] = X_test['underlyingtype'].map(mean_underlyingtype).fillna(X_train['type'].mean())

# Calculer le mean encoding pour 'product type'
mean_producttype = X_train.groupby('product type')['type'].mean()
X_train['producttype_encoded'] = X_train['product type'].map(mean_producttype)
X_test['producttype_encoded'] = X_test['product type'].map(mean_producttype).fillna(X_train['type'].mean())

# Supprimer la colonne 'type' ajoutée temporairement à X_train si nécessaire
X_train.drop('type', axis=1, inplace=True)

# Vérification : affichage des premières lignes pour contrôler
print(X_train.head())
print(X_test.head())
