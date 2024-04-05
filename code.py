# First, let's simulate the CSV files by creating them with the same columns.
# Since I don't have the exact content, I'll create a generic example based on the description.
import pandas as pd
from io import StringIO

# Example content for the CSV files
csv_content = """id,name,last_column
1,Alice,Description<br />#Tag1:Value1<br />#Tag2:Value2
2,Bob,Another description<br />#Tag1:Value3<br />#Tag3:Value4
3,Charlie,Yet another one<br />#Tag2:Value5<br />#Tag4:Value6"""

# Creating three StringIO objects to simulate files
f1 = StringIO(csv_content)
f2 = StringIO(csv_content)
f3 = StringIO(csv_content)

# Reading the CSV files into DataFrames
df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)
df3 = pd.read_csv(f3)

# Verifying that all DataFrames have the same columns
if (df1.columns == df2.columns).all() and (df2.columns == df3.columns).all():
    print("All files have the same columns.")
    # Concatenating the DataFrames into one
    dfit = pd.concat([df1, df2, df3], ignore_index=True)
    print("DataFrames concatenated into 'dfit'.")
else:
    print("The files do not have the same columns.")

# Now, let's split the last column into multiple columns based on the provided separator '<br />#'
# and rename the first new column to "description" and the following ones based on the content between '#' and ':'

# Splitting the last column and expanding into separate columns
split_columns = dfit.iloc[:, -1].str.split('<br />#', expand=True)

# Renaming the first new column to "description"
split_columns.rename(columns={0: 'description'}, inplace=True)

# For the subsequent columns, extract the name from the content
for col in split_columns.columns[1:]:
    # Extracting the text between '#' and ':' for column names
    first_row_value = split_columns[col].iloc[0] if split_columns[col].iloc[0] is not None else ""
    column_name = first_row_value.split(':')[0] if ':' in first_row_value else f"Extra_{col}"
    split_columns.rename(columns={col: column_name}, inplace=True)

# Combining the original DataFrame (without the last column) with the newly created columns
dfit = pd.concat([dfit.iloc[:, :-1], split_columns], axis=1)

# Pour corriger les nouvelles colonnes afin qu'elles ne contiennent que la valeur (et non le tag),
# nous allons retirer le nom du tag et le ':' de chaque cellule de ces colonnes.

# Retrait du nom du tag et ':' de chaque cellule pour les colonnes après "description"
for col in split_columns.columns[1:]:
    split_columns[col] = split_columns[col].str.split(':').str[1]

# Combinaison des colonnes corrigées avec le reste du DataFrame
dfit_corrected = pd.concat([dfit.iloc[:, :2], split_columns], axis=1)

dfit_corrected.head()
