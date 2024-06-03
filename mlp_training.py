import pandas as pd

# Sample data based on the image and previous context
data = {
    'ProductType': [
        'Share', 'IndexForward', 'SouitLeg', 'SecondaryShare', 'RateLeg', 
        'FictitiousShare', 'CertificateLeg', 'OptionLeg', 'ADR', 'ClosedEndFund', 
        'DividendLeg', 'PlainVanillaCall', 'PlainVanillaPut', 'Tracker', 
        'IndexFuture', 'OpenEndFund', 'BasketForward', 'StockFuture', 'StockForward'
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Define a mapping for ProductType to ProductTypeGroup
product_type_group_mapping = {
    'Share': 'Equities',
    'SecondaryShare': 'Equities',
    'FictitiousShare': 'Equities',
    'ADR': 'Equities',
    'OptionLeg': 'Derivatives',
    'PlainVanillaCall': 'Derivatives',
    'PlainVanillaPut': 'Derivatives',
    'IndexForward': 'Derivatives',
    'StockForward': 'Derivatives',
    'BasketForward': 'Derivatives',
    'IndexFuture': 'Derivatives',
    'StockFuture': 'Derivatives',
    'RateLeg': 'Fixed Income',
    'CertificateLeg': 'Fixed Income',
    'DividendLeg': 'Fixed Income',
    'ClosedEndFund': 'Funds',
    'OpenEndFund': 'Funds',
    'SouitLeg': 'Other',
    'Tracker': 'Other'
}

# Replace ProductType with ProductTypeGroup
df['ProductTypeGroup'] = df['ProductType'].map(product_type_group_mapping)

# Drop the original ProductType column
df = df.drop(columns=['ProductType'])

# Display the updated DataFrame
print(df)
