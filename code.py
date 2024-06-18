filtered_df_situation = df_situation.merge(df_partial, on=['inci_date', 'City', 'Street'], how='inner')
