from spreadsheet import Spreadsheet
from flight_details import Flight

spreadsheet = Spreadsheet()
flight_details = Flight()

data = spreadsheet.get_data()

prices = flight_details.get_price(data)
print(prices)

for city in data:
    city_price = float(city["Price"])
    
    if city["City"] in prices:
        if city_price >= float(prices[city["City"]]):
            print(f"The price for {city['City']} is within your budget: {city_price} <= {prices[city['City']]}")
        else:
            print(f"The price for {city['City']} exceeds your budget: {city_price} > {prices[city['City']]}")
    else:
        print(f"Price not available for {city['City']}")
