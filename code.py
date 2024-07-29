import pandas as pd

class PnLIncidentScope:
    """
    This class contains the perimeters and dates affected by an incident on the PnL.
    """

    def __init__(self, it_incident_folder_path, booking_incident_folder_path, referential_incident_folder_path):
        self.full_scope_it_incident = pd.read_csv(it_incident_folder_path)
        self.full_scope_booking_incident = pd.read_csv(booking_incident_folder_path)
        self.full_scope_referential_incident = pd.read_csv(referential_incident_folder_path)

    def select_pnl(self):
        # Select rows describing a PnL incident
        self.pnl_scope_it_incident = self.full_scope_it_incident[self.full_scope_it_incident['Metrics'].str.contains('Eco PnL', case=False, na=False)].copy()
        self.pnl_scope_booking_incident = self.full_scope_booking_incident[self.full_scope_booking_incident['ScopeOfData'].str.contains('Eco PnL', case=False, na=False)].copy()
        self.pnl_scope_referential_incident = self.full_scope_referential_incident[self.full_scope_referential_incident['ScopeOfData'].str.contains('Eco PnL', case=False, na=False)].copy()

    def correct_dates(self):
        # Convert date columns to datetime
        self.pnl_scope_it_incident['ValueDate'] = pd.to_datetime(self.pnl_scope_it_incident['ValueDate'])
        self.pnl_scope_booking_incident['MGASOfDate'] = pd.to_datetime(self.pnl_scope_booking_incident['MGASOfDate'])
        self.pnl_scope_referential_incident['MGASOfDate'] = pd.to_datetime(self.pnl_scope_referential_incident['MGASOfDate'])

        # Adjust dates due to a general bug: the booking data are offset by one day
        self.pnl_scope_booking_incident['MGASOfDate'] = self.pnl_scope_booking_incident['MGASOfDate'] - pd.DateOffset(days=1)

    def concatenate(self):
        # Standardize column names
        self.pnl_scope_it_incident.rename(columns={'ValueDate': 'Incident_date', 'GRPCP2C': 'grpcp200', 'GOP': 'gop'}, inplace=True)
        self.pnl_scope_booking_incident.rename(columns={'MGASOfDate': 'Incident_date', 'GRPCP2C': 'grpcp200', 'GOP': 'gop'}, inplace=True)
        self.pnl_scope_referential_incident.rename(columns={'MGASOfDate': 'Incident_date', 'GRPCP2C': 'grpcp200', 'GOP': 'gop'}, inplace=True)

        # Add a 'Type' column to identify the source of the incident
        self.pnl_scope_it_incident['Type'] = 'IT'
        self.pnl_scope_booking_incident['Type'] = 'BOOKING'
        self.pnl_scope_referential_incident['Type'] = 'REFERENTIAL'

        # Concatenate all scopes into a single DataFrame
        self.pnl_scope_incident = pd.concat([self.pnl_scope_it_incident, self.pnl_scope_booking_incident, self.pnl_scope_referential_incident], ignore_index=True)

    def select(self):
        # Select relevant columns
        columns_to_select = ['Incident_date', 'grpcp200', 'gop', 'Portfolio', 'Type']
        self.pnl_scope_incident = self.pnl_scope_incident[columns_to_select].copy()

        # Filter rows based on specific conditions
        self.pnl_scope_incident = self.pnl_scope_incident[self.pnl_scope_incident['grpcp200'].str.contains('EQUITY', case=False, na=False)].copy()
        self.pnl_scope_incident = self.pnl_scope_incident[self.pnl_scope_incident['gop'].str.contains('XF', case=False, na=False)].copy()

    def process(self):
        self.select_pnl()
        self.correct_dates()
        self.concatenate()
        self.select()
        return self.pnl_scope_incident

if __name__ == '__main__':
    it_incident_path = 'path_to_it_incident_file.csv'
    booking_incident_path = 'path_to_booking_incident_file.csv'
    referential_incident_path = 'path_to_referential_incident_file.csv'

    scope = PnLIncidentScope(it_incident_path, booking_incident_path, referential_incident_path)
    result = scope.process()
    print(result.head())
