def process_batch(sub_df, final_result):
    incidence_type = pd.crosstab(sub_df['Underlying Name'], sub_df['ProductTypeGroup'])
    incidence_perimetre = pd.crosstab(sub_df['Underlying Name'], sub_df['Portfolio'])
    
    # Vérification des NaN après crosstab
    if incidence_type.isnull().values.any():
        print("NaN detected in incidence_type after crosstab")
    if incidence_perimetre.isnull().values.any():
        print("NaN detected in incidence_perimetre after crosstab")
    
    cooccurrence_type = incidence_type.dot(incidence_type.T)
    cooccurrence_perimetre = incidence_perimetre.dot(incidence_perimetre.T) * 2
    
    # Vérification des NaN après dot product
    if cooccurrence_type.isnull().values.any():
        print("NaN detected in cooccurrence_type after dot product")
    if cooccurrence_perimetre.isnull().values.any():
        print("NaN detected in cooccurrence_perimetre after dot product")
    
    cooccurrence = cooccurrence_type + cooccurrence_perimetre
    
    # Vérification des NaN après addition des matrices
    if cooccurrence.isnull().values.any():
        print("NaN detected in cooccurrence after adding matrices")
    
    final_result.loc[cooccurrence.index, cooccurrence.columns] += cooccurrence
    
    # Vérification des NaN après mise à jour du final_result
    if final_result.isnull().values.any():
        print("NaN detected in final_result after updating with cooccurrence")
    
    return final_result

# Itération sur les batches
for start in range(0, n_data, batch_size):
    end = start + batch_size
    batch_df = x_train_string_reduced[start:end]
    final_result = process_batch(batch_df, final_result)
    progress = int((start + batch_size) * 100 / n_data)
    print(f"Progress: {progress:.2f}% completed")

# Mettre la diagonale à zéro
np.fill_diagonal(final_result.values, 0)

# Affichage de la matrice finale de cooccurrence
print(final_result.head())
