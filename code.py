# Function to create bar plots for each string column
def plot_value_counts(df):
    string_columns = df.select_dtypes(include=['object']).columns
    num_columns = len(string_columns)
    
    fig, axes = plt.subplots(num_columns, 1, figsize=(10, 5 * num_columns))

    if num_columns == 1:
        axes = [axes]
        
    for ax, column in zip(axes, string_columns):
        value_counts = df[column].value_counts()
        value_counts.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title(f"Value Counts for '{column}'")
        ax.set_xlabel('Values')
        ax.set_ylabel('Counts')
        ax.grid(axis='y')

    plt.tight_layout()
    plt.show()

# Call the function to plot the graphs
plot_value_counts(df)