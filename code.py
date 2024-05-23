# Updating the incidents data
incidents_data = {
    'incident_id': [101],
    'group_or_portfolio': ['A'],
    'comment': [
        'Issue with deal listfzhifdjnghnzri@@cnc@TD_XKDI'
    ]
}
incidents_df = pd.DataFrame(incidents_data)

# Preprocessing the comments
def preprocess_comment(comment):
    # Tokenization: split by spaces
    tokens = comment.split()
    # Remove punctuation and short tokens unless they contain uppercase letters, digits, or special characters
    tokens = [word for word in tokens if (
        word.isalnum() and len(word) > 1 and not word[0].isupper()
        or any(char.isupper() for char in word)
        or any(char.isdigit() for char in word)
        or any(not char.isalnum() for char in word)
    )]
    # Remove common stopwords except specified ones
    custom_stopwords = {'a', 'an', 'the', 'is', 'in', 'on', 'with', 'and', 'for', 'of', 'to', 'has', 'have', 'had'} - {'all', 'entire'}
    tokens = [word for word in tokens if word.lower() not in custom_stopwords]
    return tokens

incidents_df['processed_comment'] = incidents_df['comment'].apply(preprocess_comment)

# Display the tokenized message
tokenized_message = incidents_df['processed_comment'].iloc[0]

# Extracting information from the comments
def extract_info_from_comment(tokens, deals_df):
    deal_ids = set()
    portfolio_ids = set()
    features = {}
    
    for token in tokens:
        # Check if the token is a deal, portfolio, or group ID
        if token in deals_df['deal_id'].values:
            deal_ids.add(token)
        elif token in deals_df['portfolio_id'].values:
            portfolio_ids.add(token)
        elif token.isupper() and len(token) > 3:
            if token in deals_df['portfolio_id'].values:
                portfolio_ids.add(token)
        elif '=' in token:
            feature, value = token.split('=')
            if feature in deals_df.columns:
                features[feature] = value
    
    # Identify impacted deals
    affected_deals = set()
    
    if deal_ids:
        affected_deals.update(deals_df[deals_df['deal_id'].isin(deal_ids)].index)
    if portfolio_ids:
        affected_deals.update(deals_df[deals_df['portfolio_id'].isin(portfolio_ids)].index)
    for feature, value in features.items():
        if value.isdigit():
            value = int(value)
        affected_deals.update(deals_df[deals_df[feature] == value].index)
    
    return list(affected_deals)

def flag_deals(deals_df, incidents_df):
    deals_df['flag'] = 0
    
    for _, incident in incidents_df.iterrows():
        affected_deals = extract_info_from_comment(incident['processed_comment'], deals_df)
        deals_df.loc[affected_deals, 'flag'] = 1
    
    return deals_df

flagged_deals_df = flag_deals(deals_df, incidents_df)

tokenized_message, flagged_deals_df
