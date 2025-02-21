import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

sheetdb_token = os.getenv("SHEETDB_TOKEN")


class Spreadsheet:
    def __init__(self):
        self.token = sheetdb_token
        self.access_token = None
        self.data = None

    def get_data(self):
        sheetdb_url = "https://sheetdb.io/api/v1/40inzcai78gw2"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(sheetdb_url, headers=header)
        if response.status_code == 200:
            self.data = response.json()
            pprint(self.data)
            return self.data
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

