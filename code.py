# Comptage des incidents par GOP
gop_incidents = df['gop'].value_counts()

# Visualisation
gop_incidents.plot(kind='bar', color='skyblue')
plt.title('Nombre d’Incidents par GOP')
plt.xlabel('GOP')
plt.ylabel('Nombre d’Incidents')
plt.xticks(rotation=45)
plt.show()


# Comptage des incidents par Portfolio
portfolio_incidents = df['portfolio'].value_counts()

# Visualisation
portfolio_incidents.plot(kind='bar', color='green')
plt.title('Nombre d’Incidents par Portfolio')
plt.xlabel('Portfolio')
plt.ylabel('Nombre d’Incidents')
plt.xticks(rotation=45)
plt.show()

# Préparation des données
df['month'] = df['startTime'].dt.to_period('M')

# Aggrégation des données
incidents_time_gop = df.groupby(['month', 'gop']).size().unstack().fillna(0)

# Visualisation
incidents_time_gop.plot(kind='line', marker='o')
plt.title('Tendance des Incidents par Mois et par GOP')
plt.xlabel('Mois')
plt.ylabel('Nombre d’Incidents')
plt.legend(title='GOP')
plt.show()

# Aggrégation des données
type_gop_distribution = pd.crosstab(df['gop'], df['type'])

# Visualisation avec un stacked bar chart
type_gop_distribution.plot(kind='bar', stacked=True)
plt.title('Répartition des Types d’Incidents par GOP')
plt.xlabel('GOP')
plt.ylabel('Nombre d’Incidents')
plt.xticks(rotation=0)
plt.show()
