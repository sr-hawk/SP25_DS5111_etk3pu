import subprocess
import os
import datetime
import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        self.url = 'https://finance.yahoo.com/gainers'
        self.output_file = 'timed_data/ygainers.html'

    def download(self):
        print("Downloading yahoo gainers")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True) # Ensure directory exists
        command = f"sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '{self.url}' > {self.output_file}"
        subprocess.run(command, shell=True, check=True)

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        self.input_file = 'timed_data/ygainers.html'
        self.output_file = 'timed_data/ygainers.csv'

    def normalize(self):
        print("Normalizing yahoo gainers")
        try:
            raw = pd.read_html(self.input_file)
            if raw and len(raw) > 0:
                df = raw[0]
                # Extract the desired columns
                df = df[['Symbol', 'Price', 'Change', 'Change %']]
                # Rename the columns
                df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
                return df
            else:
                print("Error: No data found in Yahoo HTML.")
                return None
        except Exception as e:
            print(f"Error during normalize (Yahoo): {e}")
            return None

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
        df = self.normalize()
        if df is not None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamped_output_file = f"timed_data/ygainers_{timestamp}.csv"
            df.to_csv(timestamped_output_file, index=False)
            print(f"Saved to {timestamped_output_file}")
        else:
            print("Error: DataFrame is None. Cannot save.")
