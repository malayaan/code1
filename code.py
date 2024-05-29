import pandas as pd
import csv

def read_custom_csv(file_path, delimiter):
    rows = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        header = next(reader)  # Lire l'en-tête
        for row in reader:
            # Séparer manuellement les colonnes
            parts = row[0].split(',')
            if len(parts) >= 3:
                col1 = parts[0]
                col2 = parts[1]
                col3 = ','.join(parts[2:])
                rows.append([col1, col2, col3])

    # Créer un DataFrame
    df = pd.DataFrame(rows, columns=['col1', 'col2', 'col3'])
    return df

# Exemple d'utilisation
file_path = 'path/to/your/file.csv'
delimiter = ';;;;;'
df = read_custom_csv(file_path, delimiter)
print(df)
