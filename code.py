# Afficher les premières lignes pour avoir un aperçu des données
print(df.head())

# Résumé statistique des données numériques
print(df.describe())

# Visualisation de la distribution de chaque variable numérique
fig, axs = plt.subplots(nrows=len(df.columns), figsize=(8, 4 * len(df.columns)))
for i, col in enumerate(df.select_dtypes(include=[np.number]).columns):
    sns.histplot(df[col], kde=True, ax=axs[i])
    axs[i].set_title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# Box plots pour visualiser les potentiels valeurs aberrantes
fig, axs = plt.subplots(nrows=len(df.columns), figsize=(8, 4 * len(df.columns)))
for i, col in enumerate(df.select_dtypes(include=[np.number]).columns):
    sns.boxplot(x=df[col], ax=axs[i])
    axs[i].set_title(f'Box plot of {col}')
plt.tight_layout()
plt.show()
