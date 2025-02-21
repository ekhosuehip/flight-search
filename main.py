from spreadsheet import Spreadsheet
from flight_details import Flight
from notification import Notify

spreadsheet = Spreadsheet()
flight_details = Flight()
notifucation = Notify()

data = spreadsheet.get_data()

prices = flight_details.get_price(data)


for city in data:
    city_price = float(city["Price"])
    
    if city["City"] in prices:
        if city_price >= float(prices[city["City"]]):
            text = f"Get ready to fly🛩️, the price for {city['City']} is within your budget💵: {city_price} <= {prices[city['City']]}"
            notifucation.send_sms(text)
  
