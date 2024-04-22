import pandas as pd

# Charger votre dataframe, supposons qu'il s'appelle df
# Assurez-vous que les colonnes sont correctement formatées, en particulier les dates

# Grouper les données par date et par emplacement (ville et rue dans cet exemple)
grouped = df.groupby(['ValueDate', 'GRPC200', 'GOP'])

# Calculer le nombre total d'incidents dans le dataframe
total_incidents = len(df)

# Initialiser le compteur pour les incidents rapportés plus d'une fois par différentes personnes
duplicate_incidents_different_reporters = 0

for name, group in grouped:
    if group['RequestedForPerson.Name'].nunique() > 1:  # Plus d'une personne a reporté
        # Compter le nombre de duplicatas par groupe en excluant les duplicatas du même reporter
        duplicate_incidents_different_reporters += group.drop_duplicates(subset=['Symptom', 'RequestedForPerson.Name']).shape[0]

# Calculer le pourcentage de duplicatas rapportés par différentes personnes
percentage = (duplicate_incidents_different_reporters / total_incidents) * 100

print(f"Le pourcentage total d'incidents rapportés au même endroit et le même jour par des personnes différentes est: {percentage:.2f}%")
