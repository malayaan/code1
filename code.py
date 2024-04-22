import pandas as pd

# Supposons que votre dataframe s'appelle df
# Assurez-vous que la colonne de dates est au format datetime
df['date'] = pd.to_datetime(df['date'])

# Grouper les données par date, ville, et rue
grouped = df.groupby(['date', 'ville', 'rue'])

# Analyser chaque groupe pour déterminer les différents types d'incidents reportés
results = []

for name, group in grouped:
    # Compter le nombre total d'incidents uniques par combinaison de descriptions et de reporters
    unique_incidents = group.groupby(['description', 'email']).size().reset_index(name='counts')
    
    # Compter le nombre d'incidents uniques par description, peu importe qui reporte
    incident_counts = unique_incidents['description'].value_counts()
    
    # Identifier les situations où plusieurs personnes ont reporté le même type d'incident
    multiple_reports_same_issue = incident_counts[incident_counts > 1].sum()
    
    # Calculer le pourcentage de reports où l'incident a été rapporté par différentes personnes mais avec la même description
    if group['email'].nunique() > 1:  # Si plus d'une personne a reporté
        same_day_place = len(group)
        if same_day_place > 0:
            percentage = (multiple_reports_same_issue / same_day_place) * 100
        else:
            percentage = 0
        results.append((name, percentage))

# Créer un nouveau dataframe pour les résultats
results_df = pd.DataFrame(results, columns=['group', 'percentage_of_same_reports'])

# Afficher les résultats
print(results_df)
