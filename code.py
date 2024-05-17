# Select the combinations of pricingdate and Gop in not_a_new_deal_situation
not_a_new_deal_situation = df_concatenated[df_concatenated['SensisLastBusinessDayGop (Countervaluated)'].isnull()][['pricingdate', 'Gop']].drop_duplicates()

# Create a set of tuples for fast lookup
not_a_new_deal_set = set(not_a_new_deal_situation.apply(tuple, axis=1))

# Define a function to apply
def replace_na_if_not_in_set(row, lookup_set):
    if pd.isna(row['SensisLastBusinessDayGop (Countervaluated)']) and (row['pricingdate'], row['Gop']) not in lookup_set:
        return 0
    return row['SensisLastBusinessDayGop (Countervaluated)']

# Apply the function
df_concatenated['SensisLastBusinessDayGop (Countervaluated)'] = df_concatenated.apply(lambda row: replace_na_if_not_in_set(row, not_a_new_deal_set), axis=1)

# Display the modified DataFrame
print(df_concatenated)