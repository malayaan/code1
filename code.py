from datetime import timedelta, datetime

# Liste des jours fériés spécifiques
holidays = ['2023-01-01', '2024-01-01', '2023-12-25', '2024-12-25']

def last_business_day(date):
    # Convertir la date en datetime si ce n'est pas déjà un objet datetime
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    
    # Reculer d'un jour jusqu'à ce que vous trouviez un jour ouvrable qui n'est pas un jour férié
    while date.weekday() >= 5 or date.strftime('%Y-%m-%d') in holidays:
        date -= timedelta(days=1)
    return date

# Exemple d'utilisation:
date_example = datetime(2023, 1, 2)  # C'est un lundi, le jour après le Nouvel An
print("Original date:", date_example)
print("Last business day:", last_business_day(date_example))
