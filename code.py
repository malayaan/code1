import pandas as pd
import numpy as np
from datetime import timedelta, datetime

# Définition des jours fériés
holidays = ['2023-01-01', '2024-01-01', '2023-12-25', '2024-12-25']

def is_business_day(date):
    return date.weekday() < 5 and date.strftime('%Y-%m-%d') not in holidays

# Définir la plage de dates pour générer des paires aléatoires
date_range_start = df_expanded['Incident_date'].min()
date_range_end = df_expanded['Incident_date'].max()

# Pour stocker les nouvelles lignes
additional_rows = []

# Pour chaque 'gop' dans le DataFrame original, ajouter des paires de dates
for gop in df_expanded['gop'].unique():
    existing_dates = set(df_expanded[df_expanded['gop'] == gop]['Incident_date'])
    count = 0
    attempts = 0

    # Essayer de trouver 3 paires de dates qui ne sont pas dans le DataFrame
    while count < 3 and attempts < 3 * len(existing_dates):
        random_day = np.random.randint(0, (date_range_end - date_range_start).days)
        random_date = date_range_start + timedelta(days=random_day)
        
        if is_business_day(random_date):
            random_date_next = random_date + timedelta(days=1)
            if is_business_day(random_date_next) and random_date not in existing_dates and random_date_next not in existing_dates:
                additional_rows.append({'Incident_date': random_date, 'gop': gop})
                additional_rows.append({'Incident_date': random_date_next, 'gop': gop})
                existing_dates.update([random_date, random_date_next])
                count += 1
        attempts += 1

# Ajouter les nouvelles lignes au DataFrame existant
additional_rows_df = pd.DataFrame(additional_rows)
df_final = pd.concat([df_expanded, additional_rows_df], ignore_index=True)

# Supprimer les doublons si nécessaire
df_final = df_final.drop_duplicates(subset=['Incident_date', 'gop'])
