# Filtre pour garder uniquement les cas où le count est exactement trois
three_reports = grouped_reports[grouped_reports['count'] == 3]

# Récupérer les indices des incidents correspondants dans le DataFrame original
incident_indices = df.reset_index().merge(three_reports, on=['ValueDate', 'GRPPC200', 'GOP', 'RequestedForPerson.Name'])['index']

# Afficher les lignes concernées, regroupées par périmètre et reporter
detailed_incidents = df.loc[incident_indices].sort_values(by=['ValueDate', 'GRPPC200', 'GOP', 'RequestedForPerson.Name'])

# Imprimer chaque groupe séparément pour une meilleure lisibilité
for _, group in detailed_incidents.groupby(['ValueDate', 'GRPPC200', 'GOP', 'RequestedForPerson.Name']):
    # Vous pouvez récupérer les valeurs de périmètre et analyste ici si nécessaire
    perimeter = group['GRPPC200'].iloc[0]  # Par exemple
    analyste = group['RequestedForPerson.Name'].iloc[0]  # Par exemple
    print(f"\nIncidents rapportés par {analyste} pour le périmètre {perimeter}:")
    print(group, "\n")
