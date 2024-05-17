import matplotlib.pyplot as plt

# Sort the pricingdate values in chronological order
sorted_dates = sorted(df_concatenated[df_concatenated['Gop'] == gop_value]['pricingdate'].unique())

# Iterate over the sorted dates
for date_value in sorted_dates:
    # Filter the DataFrame based on the current combination
    df_concatenated_combination = df_concatenated[(df_concatenated['Gop'] == gop_value) & (df_concatenated['pricingdate'] == date_value)]
    
    # Get the top 10 rows with the largest absolute Daily_Pnl_Variation_Percentage
    top_10 = df_concatenated_combination.nlargest(10, 'abs_daily_pnl_variation_percentage')
    
    # Get the corresponding Daily_Pnl_Variation_Gop value from df_gop_day
    daily_pnl_variation_gop = df_gop_day[(df_gop_day['Gop'] == gop_value) & (df_gop_day['pricingdate'] == date_value)]['Daily_Pnl_Variation_Gop'].values[0]
    
    # Plot the graph with the updated title
    plt.figure(figsize=(10, 6))
    plt.bar(top_10['Deal Id'], top_10['Daily_Pnl_Variation_Percentage'], color='blue')
    
    # Formatting the x-axis to remove the time part
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter(top_10['Deal Id'].values))
    
    # Formatting the y-axis to limit the number of digits after the decimal
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
    
    # Adding horizontal line at y=0
    plt.axhline(0, color='black', linewidth=0.8)
    
    # Adding labels and title with better formatting
    plt.xlabel('Deal Id')
    plt.ylabel('Daily Pnl Variation Percentage')
    plt.title(f'{gop_value} - {date_value.strftime("%Y-%m-%d")} (Daily Pnl Variation Gop: {daily_pnl_variation_gop:.2f})')
    
    # Rotating x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
