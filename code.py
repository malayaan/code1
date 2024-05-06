from datetime import timedelta, datetime

# Liste des jours fériés (exemple pour la France, vous devrez ajuster cette liste)
holidays = ['2023-01-01', '2023-04-10', '2023-05-01', '2023-05-08', '2023-05-18', '2023-06-05', '2023-07-14', '2023-08-15', '2023-11-01', '2023-11-11', '2023-12-25']

def last_business_day(date):
    if isinstance(date, str):
        date = pd.to_datetime(date)

    # Reculer d'un jour jusqu'à ce que vous trouviez un jour ouvrable qui n'est pas un jour férié
    while date.weekday() >= 5 or date.strftime('%Y-%m-%d') in holidays:
        date -= timedelta(days=1)
    return date