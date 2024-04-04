import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Pour un style de graphique amélioré

# Charger les données
df = pd.read_csv('path_to_your_file.csv')

# Convertir les colonnes de temps en datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Créer de nouvelles colonnes pour le jour de la semaine et le mois
df['Day_of_Week'] = df['Start_Time'].dt.day_name()
df['Month'] = df['Start_Time'].dt.month_name()

# Analyser les problèmes informatiques par jour de la semaine
weekly_issues = df.groupby('Day_of_Week').size().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Visualiser les résultats pour les jours de la semaine
plt.figure(figsize=(10, 6))
sns.barplot(x=weekly_issues.index, y=weekly_issues.values)
plt.title('Number of IT Issues by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# Analyser les problèmes informatiques par mois
monthly_issues = df.groupby('Month').size().reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Visualiser les résultats pour les mois
plt.figure(figsize=(12, 7))
sns.barplot(x=monthly_issues.index, y=monthly_issues.values)
plt.title('Number of IT Issues by Month')
plt.xlabel('Month')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
