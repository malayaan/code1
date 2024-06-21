import pandas as pd

# Création d'un exemple de DataFrame
data = {
    'category': ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat1', 'cat2', 'cat3']
}
df = pd.DataFrame(data)

# Application du One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['category'])

print(df_encoded)
