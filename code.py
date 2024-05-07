from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Exemple de données textuelles
texts = [
    "chatbot technology advances rapidly",
    "natural language processing and chatbot enhancements",
    "new advances in artificial intelligence",
    "developing a smarter chatbot using NLP",
    "AI and machine learning revolutionize automation"
]

# Création du CountVectorizer
vectorizer = CountVectorizer()

# Appliquer le vectorizer aux données textuelles pour obtenir la matrice BoW
bow_matrix = vectorizer.fit_transform(texts)

# Convertir la matrice BoW en DataFrame pandas
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Afficher le DataFrame
print(bow_df)