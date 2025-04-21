import subprocess
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.url = 'https://www.wsj.com/market-data/stocks/us/movers'
        self.output_file = 'timed_data/wsjgainers.html'

    def download(self):
        print("Downloading WSJ gainers with Selenium")
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)

        try:
            # Wait for the table to load (adjust the timeout as needed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table")) # Find table.
            )
            html = driver.page_source
            with open(self.output_file, "w") as f:
                f.write(html)
        except Exception as e:
            print(f"Error downloading WSJ data: {e}")
        finally:
            driver.quit()

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        self.input_file = 'timed_data/wsjgainers.html'
        self.output_file = 'timed_data/wsjgainers.csv'

    def normalize(self):
        print("Normalizing WSJ gainers")
        try:
            raw = pd.read_html(self.input_file) # Selenium should have put a table here.
            if raw and len(raw) > 0:
                df = raw[0]
                df = df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
                df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
                return df
            else:
                print("Error: No data found in WSJ HTML.")
                return None
        except Exception as e:
            print(f"Error during normalize (WSJ): {e}")
            return None

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
        df = self.normalize()
        if df is not None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamped_output_file = f"timed_data/wsjgainers_{timestamp}.csv"
            df.to_csv(timestamped_output_file, index=False)
            print(f"Saved to {timestamped_output_file}")
        else:
            print("Error: DataFrame is None (WSJ). Cannot save.")
