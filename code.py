import category_encoders as ce

# Supposons que X_train, X_test, y_train, y_test sont déjà définis
# et que 'col1' et 'col2' sont les colonnes catégorielles dans X_train et X_test.

# Initialisation de l'encodeur avec la spécification des colonnes à encoder
encoder = ce.TargetEncoder(cols=['col1', 'col2'])

# Fit l'encodeur uniquement sur les données d'entraînement
encoder.fit(X_train, y_train)

# Transformer les données d'entraînement et de test
X_train_encoded = encoder.transform(X_train)
X_test_encoded = encoder.transform(X_test)

# Vérification des données encodées
print(X_train_encoded.head())
print(X_test_encoded.head())

pip install category_encoders
