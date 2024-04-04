import pandas as pd

def load_and_filter_data(file_path):
    # Charger les données
    df = pd.read_csv(file_path)
    
    # Convertir les colonnes de temps, en marquant les erreurs comme NaN
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')
    
    # Identifier les lignes avec des données de temps problématiques
    problematic_rows = df[df['Start_Time'].isna() | df['End_Time'].isna()]
    
    return problematic_rows

# Chemin vers votre fichier CSV
file_path = 'path_to_your_file.csv'

# Appeler la fonction et récupérer les lignes problématiques
problematic_data = load_and_filter_data(file_path)

# Afficher les lignes problématiques
if not problematic_data.empty:
    print("Problematic rows with incorrect time data:")
    print(problematic_data)
else:
    print("No problematic time data found in the file.")

