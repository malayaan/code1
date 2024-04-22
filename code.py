import pandas as pd

# Charger votre dataframe
# Assurez-vous que les colonnes de date sont au format datetime

# Grouper les données par date et périmètre
grouped = df.groupby(['ValueDate', 'GRPPC200', 'GOP'])

# Initialiser les compteurs
total_duplicates = 0
duplicates_same_reporter = 0
duplicates_different_reporters = 0

# Parcourir chaque groupe
for _, group in grouped:
    if len(group) > 1:  # Plus d'un incident dans le groupe signifie un duplicata
        total_duplicates += len(group) - 1  # Ajouter le nombre de duplicatas
        
        # Pour chaque symptôme dans le groupe, déterminer s'il a été reporté plusieurs fois par la même personne ou par des personnes différentes
        for symptom in group['Symptom'].unique():
            symptom_group = group[group['Symptom'] == symptom]
            if symptom_group['RequestedForPerson.Name'].nunique() == 1:
                duplicates_same_reporter += len(symptom_group) - 1
            else:
                duplicates_different_reporters += len(symptom_group) - 1

# Calculer les pourcentages
total_incidents = len(df)
percentage_duplicates = (total_duplicates / total_incidents) * 100
percentage_duplicates_same_reporter = (duplicates_same_reporter / total_duplicates) * 100 if total_duplicates else 0
percentage_duplicates_different_reporters = (duplicates_different_reporters / total_duplicates) * 100 if total_duplicates else 0

print(f"Pourcentage d'incidents reportés en double : {percentage_duplicates:.2f}%")
print(f"Pourcentage de ces duplicates reportés par la même personne : {percentage_duplicates_same_reporter:.2f}%")
print(f"Pourcentage de ces duplicates reportés par des personnes différentes : {percentage_duplicates_different_reporters:.2f}%")
