import pandas as pd

# Création d'un DataFrame exemple
data = {'date': pd.to_datetime(['2023-06-01', '2023-06-03', '2023-06-05', '2023-06-07'])}
df = pd.DataFrame(data)

# Calcul de la date min et max
min_date = df['date'].min()
max_date = df['date'].max()

# Génération de toutes les dates ouvrables entre min et max
all_business_days = pd.date_range(start=min_date, end=max_date, freq='B')

# Identification des dates manquantes
dates_in_df = pd.DataFrame(df['date'])
missing_dates = all_business_days[~all_business_days.isin(dates_in_df['date'])]

# Création du DataFrame des dates manquantes
df_missing_dates = pd.DataFrame(missing_dates, columns=['Missing Dates'])

# Affichage du DataFrame des dates manquantes
print(df_missing_dates)
