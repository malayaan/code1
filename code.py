# Créer un nouveau DataFrame en dupliquant chaque ligne pour J et J-1
new_rows = []
for index, row in df_concatenated.iterrows():
    # Ajouter la ligne originale
    new_rows.append(row.to_dict())
    
    # Ajouter une ligne pour J-1
    new_row = row.to_dict()
    new_row['date'] = row['date'] - timedelta(days=1)
    new_rows.append(new_row)

# Créer un nouveau DataFrame avec les nouvelles lignes
df_expanded = pd.DataFrame(new_rows)

# Convertir 'date' à nouveau en format datetime pour assurer la cohérence
df_expanded['date'] = pd.to_datetime(df_expanded['date'])

# Supprimer les doublons
df_expanded = df_expanded.drop_duplicates()

df_expanded.head()


--------------------------------------

# Définir la plage de dates pour générer des paires aléatoires
date_range_start = df_expanded['date'].min()
date_range_end = df_expanded['date'].max()

# Pour stocker les nouvelles lignes
additional_rows = []

# Pour chaque GOP dans le DataFrame original, ajouter 3 nouvelles paires de dates
for gop in df_expanded['gop'].unique():
    existing_dates = set(df_expanded[df_expanded['gop'] == gop]['date'])
    count = 0
    attempts = 0

    # Essayer de trouver 3 paires de dates qui ne sont pas déjà dans le DataFrame
    while count < 3 and attempts < 100:
        # Générer une date aléatoire
        random_date = date_range_start + timedelta(days=random.randint(0, (date_range_end - date_range_start).days))
        random_date_next = random_date + timedelta(days=1)
        
        # Vérifier si cette paire est déjà présente pour ce GOP
        if random_date not in existing_dates and random_date_next not in existing_dates:
            # Ajouter les deux nouvelles dates pour le même GOP
            additional_rows.append({'date': random_date, 'gop': gop})
            additional_rows.append({'date': random_date_next, 'gop': gop})
            
            # Enregistrer ces dates comme existantes pour éviter les doublons
            existing_dates.update([random_date, random_date_next])
            count += 1
        attempts += 1

# Ajouter les nouvelles lignes au DataFrame existant
additional_rows_df = pd.DataFrame(additional_rows)
df_final = pd.concat([df_expanded, additional_rows_df], ignore_index=True)

# Supprimer les doublons, si nécessaire (bien que cela ne devrait pas arriver avec les vérifications ci-dessus)
df_final = df_final.drop_duplicates()

# Regrouper le DataFrame par 'gop' et 'date', puis trier
df_grouped = df_final.sort_values(['gop', 'date']).groupby(['gop', 'date']).first().reset_index()

df_grouped.head(20)  # Afficher les 20 premières lignes du DataFrame groupé pour inspection

--------------------------

# Assurer que la colonne 'date' dans les deux DataFrames est au même format
df_concatenated['date'] = pd.to_datetime(df_concatenated['date'])
df_grouped['date'] = pd.to_datetime(df_grouped['date'])

# Fusionner les deux DataFrames sur 'gop' et 'date' pour récupérer la colonne 'type'
df_merged = pd.merge(df_grouped, df_concatenated[['gop', 'date', 'type']], on=['gop', 'date'], how='left')

# Remplir les valeurs manquantes de 'type' avec 'NotAIncident'
df_merged['type'] = df_merged['type'].fillna('NotAIncident')

df_merged.head(20)
