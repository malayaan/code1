import json
import re
from sklearn.feature_extraction.text import CountVectorizer

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
    ['{"Datedutruc": "2023-04-03", "metric":"var"}', ..., 'print("Hello, world!") # This is a comment'],
    ['{"Datedutruc": "2023-05-22", "metric":"var2"}', ..., 'SELECT * FROM table; -- Select statement']
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

# Affichage des résultats
print("Vocabulaire:", vectorizer.get_feature_names_out())
print("Bag of Words matrix:\n", bow_matrix.toarray())

