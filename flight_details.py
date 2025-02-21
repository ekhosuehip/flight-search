import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import requests

load_dotenv()


class Flight:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }

        response = requests.post(url, headers=header, data=params)
        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            return self.access_token
        else:
            return None
        
    def get_price(self, cities):

        if not hasattr(self, "access_token") or not self.access_token:
            self.get_token()
        
        if self.access_token:
            current_date = datetime.now().date()
            six_months = current_date + relativedelta(months=6)
            url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
            header = {
                "Authorization": f"Bearer {self.access_token}"
            }
            
            prices = {}

            for city in cities:
                params = {
                    "originLocationCode": "LON",
                    "destinationLocationCode": city["iataCode"],
                    "departureDate": six_months,
                    "adults": 1,
                    "max": 1,
                    "currencyCode": "GBP"
                }

                response = requests.get(url=url, headers=header, params=params)
                if response.status_code == 200:
                    price = response.json()["data"][0]["price"]["grandTotal"]
                    prices[city["City"]] = price
                else:
                    print(f"Error: {response.status_code} for city {city['City']}: {response.text}")
            return prices
        else:
            print("No access code")


    
