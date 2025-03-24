import subprocess
import os
import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        self.url = 'https://finance.yahoo.com/gainers'
        self.output_file = 'sample_data/ygainers.html'

    def download(self):
        print("Downloading yahoo gainers")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True) # Ensure directory exists
        command = f"sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '{self.url}' > {self.output_file}"
        subprocess.run(command, shell=True, check=True)

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        self.input_file = 'sample_data/ygainers.html'
        self.output_file = 'sample_data/ygainers.csv'

    def normalize(self):
        print("Normalizing yahoo gainers")
        raw = pd.read_html(self.input_file)
        df = raw[0]
        df.to_csv(self.output_file, index=False)

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
