from dotenv import load_dotenv
from pprint import pprint
from configs import weather_url
from utils import valid_input
import requests
import os

load_dotenv()

def get_weather_data(city="Nairobi"):
    try:
        api_key = os.getenv("API_KEY")
        request_url = f'{weather_url}&q={city.lower()}&appid={api_key}'
        response = requests.get(request_url)
        return response.json()
    except:
        return "Error in getting data"

if __name__ == "__main__":
    print("\n***** Weather App *****\n")
    city = input("Please insert a city:\n").strip()
    
    if(valid_input(city)):
        data = get_weather_data(city)
        pprint(data)
    else:
        print("Invalid inputs")
