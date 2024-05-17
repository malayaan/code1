import pandas as pd

# Conversion des dates en datetime (si ce n'est pas déjà fait)
df_concatenated['pricingdate'] = pd.to_datetime(df_concatenated['pricingdate'])

# Sélection des combinaisons de valeur pour pricingdate et Gop dans not_a_new_deal_situation
not_a_new_deal_situation = df_concatenated[df_concatenated['SensisLastBusinessDayGop (Countervaluated)'].isnull()][['pricingdate', 'Gop']].drop_duplicates()

# Ajout de la colonne 'abs_variation' si nécessaire
df_concatenated['abs_variation'] = df_concatenated['Daily_Pnl_Variation_Percentage'].abs()

# Boucle sur chaque combinaison unique de pricingdate et Gop dans df_concatenated
for index, row in df_concatenated.iterrows():
    pricingdate = row['pricingdate']
    gop = row['Gop']
    
    # Vérification si la combinaison est dans not_a_new_deal_situation
    if not ((not_a_new_deal_situation['pricingdate'] == pricingdate) & (not_a_new_deal_situation['Gop'] == gop)).any():
        # Remplacement de NaN par 0 dans 'SensisLastBusinessDayGop (Countervaluated)'
        if pd.isna(row['SensisLastBusinessDayGop (Countervaluated)']):
            df_concatenated.at[index, 'SensisLastBusinessDayGop (Countervaluated)'] = 0

# Affichage du DataFrame modifié
print(df_concatenated)
