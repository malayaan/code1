import os
import pandas as pd

class DataProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_and_concatenate_data(self):
        # Read all CSV files from the specified folder and concatenate them into a single DataFrame
        all_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.csv')]
        self.df = pd.concat([pd.read_csv(file, sep=";") for file in all_files], ignore_index=True)

    def clean_data(self):
        # Drop unnecessary columns and handle data types
        self.df.drop(columns=['Riskmetricname'], inplace=True)
        # Convert columns to datetime where appropriate
        self.df['pricingdate'] = pd.to_datetime(self.df['pricingdate'], errors='coerce')
        
        # Fill missing values
        self.df.fillna(0, inplace=True)

    def create_unique_id(self):
        # Create a unique ID based on multiple columns
        self.df['UniqueID'] = self.df['Underlying Type'] + '_' + self.df['Product Type'] + '_' + self.df['DealID'].astype(str)

    def aggregate_data(self):
        # Dictionary defining aggregation methods for each column
        agg_dict = {
            'quantity': 'sum', 'spot': 'sum', 'Quantity Incremental Change': 'sum',
            'Strike': 'sum', 'New and Modified': 'sum', 'CMPO_EFFECT': 'sum',
            'PRICINGMODEL_EFFECT': 'sum', 'FOREX_EFFECT': 'sum', 'IR_EFFECT': 'sum',
            'SPOTDIV_EFFECT': 'sum', 'SPOTFOREX_EFFECT': 'sum', 'SPOTREPO_EFFECT': 'sum',
            'THETA_EFFECT': 'sum', 'V3': 'sum', 'ZORG_EFFECT': 'sum',
            'Underlying Name': 'first', 'Underlying Type': 'first', 'Product Type': 'first',
            'Global Maturity': 'first', 'Effective Maturity': 'first', 'DealID': 'first',
            'Portfolio': 'first', 'GOP': 'first', 'GRPC': 'first'
        }
        # Aggregate data using the defined dictionary
        self.df = self.df.groupby('UniqueID').agg(agg_dict).reset_index()

    def save_data(self, output_file):
        # Save the cleaned and aggregated DataFrame to a new CSV file
        self.df.to_csv(output_file, index=False, compression='gzip')

    def process_data(self):
        self.read_and_concatenate_data()
        self.clean_data()
        self.create_unique_id()
        self.aggregate_data()
        self.save_data('dataset_no_duplicate.csv')

if __name__ == '__main__':
    folder_path = 'C:/path_to_your_data/'
    processor = DataProcessor(folder_path)
    processor.process_data()
