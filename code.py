import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import nltk

# Download necessary NLTK data
nltk.download('punkt')

# Sample DataFrame
data = {'messages': [
    "This is the first message.",
    "Here's the second message, which is longer than the first.",
    "Is this the third message?",
    "Indeed, this is the fourth message!"
]}

df = pd.DataFrame(data)

# Initialize the stemmer
stemmer = PorterStemmer()

# Function to perform stemming
def stem_message(message):
    tokens = word_tokenize(message)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

# Apply stemming to each message
df['stemmed_messages'] = df['messages'].apply(stem_message)

# Initialize the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the stemmed messages
X = vectorizer.fit_transform(df['stemmed_messages'])

# Convert to dense array
X_dense = X.toarray()

# Compute the covariance matrix
cov_matrix = np.cov(X_dense, rowvar=False)

# Initialize PCA
pca = PCA(n_components=2)  # Adjust the number of components as needed

# Fit and transform the data
reduced_data = pca.fit_transform(cov_matrix)

print("Reduced Data Shape:", reduced_data.shape)
print("Reduced Data:")
print(reduced_data)
