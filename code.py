import pandas as pd

def read_custom_csv(file_path, delimiter):
    rows = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        header = lines[0].split(',')[0:3]  # Lire l'en-tête et prendre les trois premières colonnes
        for line in lines[1:]:
            # Séparer manuellement les colonnes
            parts = line.split(delimiter)[0].split(',')
            if len(parts) >= 3:
                col1 = parts[0]
                col2 = parts[1]
                col3 = ','.join(parts[2:])
                rows.append([col1, col2, col3])

    # Créer un DataFrame
    df = pd.DataFrame(rows, columns=['col1', 'col2', 'col3'])
    return df

# Exemple d'utilisation
file_content = """col1,col2,col3;;;;;
1,2,etyduc,dfvi;;;;;
5,4,ghjkoiug giuy;;;;;"""

# Sauvegarder le contenu dans un fichier temporaire
file_path = '/mnt/data/temp_file.csv'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(file_content)

# Lire et afficher le DataFrame
delimiter = ';;;;;'
df = read_custom_csv(file_path, delimiter)
import ace_tools as tools; tools.display_dataframe_to_user(name="Custom CSV DataFrame", dataframe=df)

df
