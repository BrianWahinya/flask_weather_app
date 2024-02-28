from dotenv import load_dotenv
from pprint import pprint
from configs import weather_url
from utils import valid_input
import requests
import sys, os

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
    
    # checks for empty or spaces
    if not valid_input(city): 
        print("Invalid inputs")
        sys.exit()

    data = get_weather_data(city)
    if data['cod'] in {200, str(200)}:
        pprint(data)
        sys.exit()

    if data['cod'] in {404, str(404)}:
        print(f"Error: {city} not found")
        sys.exit()

    print(data['message'] or data)
