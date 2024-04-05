# Étape 2 : Filtrer pour janvier et février 2024
jan_feb_2024 = df[(df['start_time'].dt.month.isin([1, 2])) & (df['start_time'].dt.year == 2024)]

# Étape 3 : Compter les lignes où 'Grppc200' n'est pas NaN
count = jan_feb_2024[jan_feb_2024['Grppc200'].notna()].shape[0]

print(count)
