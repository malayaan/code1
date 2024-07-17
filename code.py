import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Assuming filtered_df is already defined and contains the data to be plotted

plt.figure(figsize=(10, 8))
well_knowned = x_train_string['Underlying Name'].values
filtered_df = embedding_df[embedding_df['Underlying Name'].isin(well_knowned)][['Underlying_name_embedding_1', 'Underlying_name_embedding_2']]

plt.figure(figsize=(8, 6))
x = filtered_df['Underlying_name_embedding_1']
y = filtered_df['Underlying_name_embedding_2']

# Create a 2D histogram (density plot)
nbins = 100
kde = sns.kdeplot(x=x, y=y, cmap='Reds', fill=True)
plt.colorbar(kde.collections[-1], ax=kde, orientation='vertical').set_label('Density')

plt.xlabel('Underlying_name_embedding_1')
plt.ylabel('Underlying_name_embedding_2')
plt.title('Density Plot with Colorbar')
plt.show()
