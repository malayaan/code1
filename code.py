import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import category_encoders as ce

# Charger les données en DataFrame Dask
ddf = dd.read_csv('your_large_file.csv')

# Convertir les colonnes catégorielles en type 'category'
ddf['col1'] = ddf['col1'].astype('category')
ddf['col2'] = ddf['col2'].astype('category')

# Encoder avec Dask (exemple fictif, adapter selon besoin)
encoder = ce.TargetEncoder(cols=['col1', 'col2'])

with ProgressBar():
    # Fit et transform sont effectués en parallèle
    ddf_encoded = encoder.fit_transform(ddf.categorize(columns=['col1', 'col2']), ddf['y'])

# Calculer et convertir en pandas DataFrame si nécessaire
df_encoded = ddf_encoded.compute()
