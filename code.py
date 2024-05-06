import pandas as pd
import numpy as np
from datetime import timedelta, datetime

# Définition des jours fériés
holidays = pd.to_datetime(['2023-01-01', '2024-01-01', '2023-12-25', '2024-12-25'])

def is_business_day(date):
    return date.weekday() < 5 and not date in holidays

# Définir la plage de dates pour générer des paires aléatoires
date_range_start = df_expanded['Incident_date'].min()
date_range_end = df_expanded['Incident_date'].max()

# Calculer tous les jours ouvrables entre la plage de dates
all_days = pd.date_range(start=date_range_start, end=date_range_end, freq='D')
business_days = [day for day in all_days if is_business_day(day)]

# Pour stocker les nouvelles lignes
additional_rows = []

# Pour chaque GOP dans le DataFrame original, ajouter des nouvelles paires de dates
for gop in df_expanded['gop'].unique():
    existing_dates = set(df_expanded[df_expanded['gop'] == gop]['Incident_date'])
    
    # Pré-calculer les paires de dates consécutives qui ne sont pas dans existing_dates
    available_days = [day for day in business_days if day not in existing_dates]
    consecutive_pairs = [(available_days[i], available_days[i + 1]) for i in range(len(available_days) - 1)
                         if (available_days[i + 1] - available_days[i]).days == 1]
    
    n = len(existing_dates)
    count = 0

    # Essayer de trouver 3*n paires de dates qui ne sont pas déjà dans le DataFrame
    while count < 3 * n and consecutive_pairs:
        random_pair = np.random.choice(len(consecutive_pairs), size=1, replace=False)[0]
        random_date, random_date_next = consecutive_pairs.pop(random_pair)

        if random_date not in existing_dates and random_date_next not in existing_dates:
            additional_rows.append({'Incident_date': random_date, 'gop': gop})
            additional_rows.append({'Incident_date': random_date_next, 'gop': gop})
            existing_dates.update([random_date, random_date_next])
            count += 1

# Ajouter les nouvelles lignes au DataFrame existant
additional_rows_df = pd.DataFrame(additional_rows)
df_final = pd.concat([df_expanded, additional_rows_df], ignore_index=True)

# Supprimer les doublons, si nécessaire (normalement ne devrait pas y en avoir)
df_final = df_final.drop_duplicates()

# Regrouper le DataFrame par 'gop' et 'date', puis trier
df_grouped = df_final.sort_values(['gop', 'Incident_date']).groupby('gop')['Incident_date'].first().reset_index()
df_grouped.head(50)  # Afficher les premières lignes du DataFrame groupé pour inspection
