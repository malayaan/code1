# Calculons la durée de vie du deal en mois
df['Deal_Life_Months'] = (df['Deal - Effective Maturity'] - df['pricingdate']) / pd.Timedelta(days=30)

# Arrondissons à l'entier le plus proche pour simplifier
df['Deal_Life_Months_Rounded'] = df['Deal_Life_Months'].round()

# Tracer la répartition des durées de vie des deals en mois
df['Deal_Life_Months_Rounded'].value_counts().sort_index().plot(kind='bar')

#
