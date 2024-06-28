import pandas as pd
import matplotlib.pyplot as plt

# Supposons que df est votre DataFrame original
# Convertir 'startTime' en datetime si ce n'est pas déjà fait
df['startTime'] = pd.to_datetime(df['startTime'], errors='coerce')
df.dropna(subset=['startTime', 'type'], inplace=True)  # Assurez-vous que les données essentielles sont présentes

# Regrouper par type et par mois, et compter les incidents
monthly_incidents_by_type = df.groupby([pd.Grouper(key='startTime', freq='M'), 'type']).size().unstack(fill_value=0)

# Cumuler les totaux pour montrer l'évolution du nombre total d'incidents
cumulative_incidents_by_type = monthly_incidents_by_type.cumsum()

# Afficher la table des incidents cumulés pour vérification
print(cumulative_incidents_by_type)
# Tracer la tendance cumulative des incidents par type
cumulative_incidents_by_type.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Évolution Cumulative des Incidents par Type et par Mois')
plt.xlabel('Mois')
plt.ylabel('Nombre Cumulé d’Incidents')
plt.grid(True)
plt.legend(title='Type d\'Incident')
plt.show()
