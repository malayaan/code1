import pandas as pd

# Supposons que 'Date', 'Périmètre', et 'Type' sont les noms finaux des colonnes que vous voulez
# Remplacez 'IncidentDate', 'GRPPC200', et 'type' par les noms réels des colonnes dans vos dataframes

# Étape 1 et 2: Filtrer et renommer les colonnes
dfit_filtered = dfit[['IncidentDate', 'GRPPC200']].rename(columns={'IncidentDate': 'Date', 'GRPPC200': 'Périmètre'})
dfbk_filtered = dfbk[['ValueDate', 'GRPPC200']].rename(columns={'ValueDate': 'Date', 'GRPPC200': 'Périmètre'})
dfrf_filtered = dfrf[['WMGSADate', 'GRPPC200']].rename(columns={'WMGSADate': 'Date', 'GRPPC200': 'Périmètre'})

# Étape 3: Ajouter une colonne 'Type'
dfit_filtered['Type'] = 'IT'
dfbk_filtered['Type'] = 'BOOKING'
dfrf_filtered['Type'] = 'REFERENTIAL'

# Étape 4: Concaténer les dataframes
df_final = pd.concat([dfit_filtered, dfbk_filtered, dfrf_filtered], ignore_index=True)

# Maintenant, df_final devrait contenir vos données concaténées
