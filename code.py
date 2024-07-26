import os
import pandas as pd
from tqdm import tqdm
import warnings

class DataProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_and_concatenate_data(self):
        all_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.csv')]
        df_list = [pd.read_csv(file, sep=";", low_memory=False) for file in all_files]
        self.df = pd.concat(df_list, ignore_index=True)

    def clean_data(self):
        self.df.drop(columns=['Riskmetricname'], inplace=True)
        self.df['pricingdate'] = pd.to_datetime(self.df['pricingdate'], errors='coerce')
        # Use a more explicit fillna to avoid chain indexing issues
        for col in self.df.columns:
            self.df[col] = self.df[col].fillna(0)

    def create_unique_id(self):
        self.df['UniqueID'] = self.df['Underlying Type'] + '_' + self.df['Product Type'] + '_' + self.df['DealID'].astype(str)

    def aggregate_data(self):
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
        self.df = self.df.groupby('UniqueID').agg(agg_dict).reset_index()

    def save_data(self, output_file):
        chunk_size = 10000  # Number of rows per chunk
        num_chunks = len(self.df) // chunk_size + 1
        mode = 'w'
        header = True

        with tqdm(total=len(self.df), desc="Saving DataFrame to CSV") as pbar:
            for i in range(num_chunks):
                start_row = i * chunk_size
                end_row = (i + 1) * chunk_size
                chunk = self.df.iloc[start_row:end_row]
                chunk.to_csv(output_file, mode=mode, header=header, index=False, compression='gzip')
                mode = 'a'  # Append mode for subsequent chunks
                header = False  # Do not write the header for subsequent chunks
                pbar.update(len(chunk))

    def process_data(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.DtypeWarning)
            self.read_and_concatenate_data()
        self.clean_data()
        self.create_unique_id()
        self.aggregate_data()
        self.save_data('dataset_no_duplicate.csv')

if __name__ == '__main__':
    folder_path = 'C:/path_to_your_data/'
    processor = DataProcessor(folder_path)
    processor.process_data()
