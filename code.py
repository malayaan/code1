import pandas as pd

# Lecture des fichiers CSV
dfit = pd.read_csv('dataframes/Unity_it_clean.csv')
dfbk = pd.read_csv('dataframes/SGWorkflow_booking_clean.csv')
dfrf = pd.read_csv('dataframes/SGWorkflow_referential_clean.csv')

# Filtre basé sur les conditions spécifiques
dfit_pnl = dfit[dfit['Metrics'].str.contains('EcoPnL', case=False, na=False)]
dfbk_pnl = dfbk[dfbk['ScopeOfData'].str.contains('EcoPnL', case=False, na=False)]
dfrf_pnl = dfrf[dfrf['ScopeOfData'].str.contains('EcoPnL', case=False, na=False)]

# Conversion des dates et renommage des colonnes
dfit_pnl['ValueDate'] = pd.to_datetime(dfit_pnl['ValueDate'])
dfbk_pnl['WMGSADate'] = pd.to_datetime(dfbk_pnl['WMGSADate'])
dfrf_pnl['WMGSADate'] = pd.to_datetime(dfrf_pnl['WMGSADate'])

dfit_pnl = dfit_pnl.rename(columns={'ValueDate': 'Incident_date', 'GRPPC200': 'Perimeter'})
dfbk_pnl = dfbk_pnl.rename(columns={'WMGSADate': 'Incident_date', 'grppc200': 'Perimeter'})
dfrf_pnl = dfrf_pnl.rename(columns={'WMGSADate': 'Incident_date', 'grppc200': 'Perimeter'})

# Ajout de la colonne 'Type'
dfit_pnl['Type'] = 'IT'
dfbk_pnl['Type'] = 'BOOKING'
dfrf_pnl['Type'] = 'REFERENTIAL'

# Sélection des colonnes pertinentes pour la concaténation
columns_to_select = ['Incident_date', 'Perimeter', 'Type']
dfit_pnl = dfit_pnl[columns_to_select]
dfbk_pnl = dfbk_pnl[columns_to_select]
dfrf_pnl = dfrf_pnl[columns_to_select]

# Concaténation des dataframes
df_concatenated = pd.concat([dfit_pnl, dfbk_pnl, dfrf_pnl], ignore_index=True)

# Résultat final
print(df_concatenated)
