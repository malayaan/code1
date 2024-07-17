import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming filtered_df is already defined and contains the data to be plotted

plt.figure(figsize=(10, 8))
well_knowned = x_train_string['Underlying Name'].values
filtered_df = embedding_df[embedding_df['Underlying Name'].isin(well_knowned)][['Underlying_name_embedding_1', 'Underlying_name_embedding_2']]

plt.figure(figsize=(8, 6))
ax = sns.kdeplot(
    x=filtered_df['Underlying_name_embedding_1'], 
    y=filtered_df['Underlying_name_embedding_2'], 
    cmap='Reds', 
    fill=True
)

# Add a colorbar to indicate density
cbar = plt.colorbar(ax.collections[0], ax=ax, orientation='vertical')
cbar.set_label('Density')

plt.show()
