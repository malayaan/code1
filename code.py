import pandas as pd

# Supposons que df_incidents et df_deals sont vos deux DataFrames

# DataFrame des incidents
# df_incidents = pd.DataFrame({
#     'IncidentDate': [...],
#     'Gop': [...],
#     'Type': [...]
# })

# DataFrame des deals
# df_deals = pd.DataFrame({
#     'PricingDate': [...],
#     'Gop': [...]
# })

# Étape 1: Renommer les colonnes pour clarifier la jointure
df_incidents = df_incidents.rename(columns={'IncidentDate': 'Date', 'Type': 'IncidentType'})
df_deals = df_deals.rename(columns={'PricingDate': 'Date'})

# Étape 2: Effectuer une jointure sur 'Gop' et 'Date'
df_merged = pd.merge(df_deals, df_incidents, on=['Gop', 'Date'], how='left')

# Étape 3: Remplir la colonne 'Type' avec 'NotAnIncident' lorsque 'IncidentType' est NaN, sinon avec 'IncidentType'
df_merged['Type'] = df_merged['IncidentType'].fillna('NotAnIncident')

# Étape 4: Supprimer la colonne intermédiaire 'IncidentType' si nécessaire
df_merged = df_merged.drop(columns=['IncidentType'])

# Étape 5: Renommer la colonne 'Date' à 'PricingDate' pour revenir à l'original
df_merged = df_merged.rename(columns={'Date': 'PricingDate'})

# df_merged est le DataFrame final avec la colonne 'Type' ajoutée
print(df_merged)
