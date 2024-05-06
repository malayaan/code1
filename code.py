from datetime import timedelta

# Liste des jours fériés spécifiques
holidays = ['2023-01-01', '2024-01-01', '2023-12-25', '2024-12-25']

def last_business_day(date):
    # Reculer d'un jour jusqu'à ce que vous trouviez un jour ouvrable qui n'est pas un jour férié
    while date.weekday() >= 5 or date.strftime('%Y-%m-%d') in holidays:
        date -= timedelta(days=1)
    return date

# Exemple d'utilisation:
import pandas as pd

# Supposons que vous avez un DataFrame avec une colonne de dates
df = pd.DataFrame({
    'Incident_date': ['2023-12-25', '2024-01-01', '2023-07-04']
})

# Convertir les chaînes en datetime si ce n'est pas déjà fait
df['Incident_date'] = pd.to_datetime(df['Incident_date'])

# Appliquer la fonction à chaque date
df['Last_Business_Day'] = df['Incident_date'].apply(last_business_day)

# Afficher le résultat
print(df)
