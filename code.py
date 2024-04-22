# Regrouper par date, périmètre, et RequestedForPerson.Name, puis compter les occurrences
grouped_reports = df.groupby(['ValueDate', 'GRPPC200', 'GOP', 'RequestedForPerson.Name']).size().reset_index(name='count')

# Filtrer pour garder uniquement les cas où il y a eu plusieurs rapports sur le même périmètre et la même date, peu importe la personne
multiple_reports = grouped_reports.groupby(['ValueDate', 'GRPPC200', 'GOP']).filter(lambda x: x['RequestedForPerson.Name'].nunique() > 1)

# Récupérer les indices des incidents correspondants dans le DataFrame original
incident_indices = df.reset_index().merge(multiple_reports, on=['ValueDate', 'GRPPC200', 'GOP'])['index']

# Afficher les lignes concernées, regroupées par périmètre et reporter
detailed_incidents = df.loc[incident_indices].sort_values(by=['ValueDate', 'GRPPC200', 'GOP', 'RequestedForPerson.Name'])

# Imprimer chaque groupe séparément pour une meilleure lisibilité
for _, group in detailed_incidents.groupby(['ValueDate', 'GRPPC200', 'GOP']):
    # Assurer que le groupe contient des rapports de plusieurs personnes
    if group['RequestedForPerson.Name'].nunique() > 1:
        # Obtenir le périmètre et la date
        date = group['ValueDate'].iloc[0]
        perimetre = group['GRPPC200'].iloc[0] + ' ' + group['GOP'].iloc[0]
        # Afficher les détails
        print(f"\nIncidents rapportés sur le périmètre {perimetre} le {date}:")
        # Itérer sur chaque ligne pour afficher les informations
        for index, row in group.iterrows():
            analyste = row['RequestedForPerson.Name']
            symptom = row['Symptom']
            print(f"Rapporté par {analyste} pour le symptôme {symptom}")
