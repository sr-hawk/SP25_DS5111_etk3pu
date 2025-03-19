import subprocess
import pandas as pd
import os
from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.url = 'https://www.wsj.com/market-data/stocks/biggest-gainers'
        self.output_file = 'sample_data/wjsgainers.html'

    def download(self):
        print("Downloading WSJ gainers")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True) # Ensure directory exists
        command = f"sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '{self.url}' > {self.output_file}"
        subprocess.run(command, shell=True, check=True)
        
class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        self.input_file = 'sample_data/wjsgainers.html'
        self.output_file = 'sample_data/wjsgainers.csv'

    def normalize(self):
        print("Normalizing WSJ gainers")
        try:
            raw = pd.read_html(self.input_file)
            df = raw[0]
            df.to_csv(self.output_file, index=False)
        except Exception as e:
            print(f"Error processing WSJ data: {e}")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")