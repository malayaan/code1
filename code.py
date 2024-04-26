# Supprimer les lignes où les colonnes de date ou de Product Type sont NaN
df_clean = df.dropna(subset=['Deal - Effective Maturity', 'pricingdate', 'Product Type'])

# À ce stade, df_clean contiendra seulement les lignes où les dates et les product types sont présents
# Convertir les dates en les vérifiant
def safe_convert_date(date_series, errors='coerce'):
    return pd.to_datetime(date_series, errors=errors)

# Appliquer la fonction de conversion en toute sécurité
df_clean['Deal - Effective Maturity'] = safe_convert_date(df_clean['Deal - Effective Maturity'])
df_clean['pricingdate'] = safe_convert_date(df_clean['pricingdate'])

# Supprimer les lignes avec des erreurs de conversion après la coercion
df_clean = df_clean.dropna(subset=['Deal - Effective Maturity', 'pricingdate'])
# Définir des limites de date raisonnables (par exemple, de 1900 à 2100)
start_date = pd.Timestamp('1900-01-01')
end_date = pd.Timestamp('2100-01-01')

# Filtrer les lignes où les dates sont à l'intérieur de la plage spécifiée
df_clean = df_clean[
    (df_clean['Deal - Effective Maturity'] >= start_date) & 
    (df_clean['Deal - Effective Maturity'] <= end_date) &
    (df_clean['pricingdate'] >= start_date) & 
    (df_clean['pricingdate'] <= end_date)
]
# Vérifier le nombre de lignes restantes
print(f"Nombre de lignes après nettoyage : {df_clean.shape[0]}")
