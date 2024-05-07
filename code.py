import json
import re
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Fonction pour supprimer les commentaires de Python et HQL
def remove_comments(code, language):
    if language == 'python':
        return re.sub(r"#.*", "", code)
    elif language == 'hql':
        code = re.sub(r"--.*", "", code)
        return re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    else:
        return code

# Liste simulée de données
data = [
    ['{"Datedutruc": "2023-04-03", "metric":"var"}', '...', 'print("Hello, world!") # This is a comment'],
    ['{"Datedutruc": "2023-05-22", "metric":"var2"}', '...', 'SELECT * FROM table; -- Select statement']
]

# Prétraitement des données pour enlever les commentaires
cleaned_data = []
for entry in data:
    json_data = json.loads(entry[0])  # Assume JSON data in the first element
    code = entry[5]  # Code in the 6th element
    
    # Déterminer le langage basé sur un champ métrique ou autre indicateur
    language = 'python' if 'py' in json_data['metric'] else 'hql'
    
    # Nettoyer les commentaires
    cleaned_code = remove_comments(code, language)
    cleaned_data.append(cleaned_code)

# Création du modèle Bag of Words
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(cleaned_data)

# Extraction des fréquences des mots et vocabulaire
word_freq = bow_matrix.sum(axis=0)
words = vectorizer.get_feature_names_out()
freq_dict = dict(zip(words, word_freq.tolist()[0]))

# Création du graphique
plt.figure(figsize=(10, 8))
plt.bar(freq_dict.keys(), freq_dict.values(), color='blue')
plt.xlabel('Mots')
plt.ylabel('Fréquence')
plt.title('Fréquence des mots dans les documents')
plt.xticks(rotation=90)  # Rotation des étiquettes pour meilleure lisibilité
plt.show()
