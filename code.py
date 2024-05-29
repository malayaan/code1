import csv

def read_custom_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Lire l'en-tête
        print(f"Header: {header}")

        for row in reader:
            # Les deux premières colonnes
            col1 = row[0]
            col2 = row[1]
            # La troisième colonne est tout ce qui suit la deuxième virgule
            col3 = ','.join(row[2:])
            print(f"Colonne 1: {col1}, Colonne 2: {col2}, Colonne 3: {col3}")

# Exemple d'utilisation
file_path = 'path/to/your/file.csv'
read_custom_csv(file_path)
