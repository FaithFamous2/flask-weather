import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city = "Lagos"):
    print('\n*** Get Current Weather Conditions ***\n')

    request_url =f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    # print(request_url)



    weather_data = requests.get(request_url).json()

    return weather_data

    # pprint(weather_data)
    print(f"\nCurrent weather data for {weather_data['name']}")
    print(f"\nCountry: {weather_data['sys']['country']}")
    print(f"\nTemp is {weather_data['main']['temp']}")
    print(f"\nFeels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}")


# get_current_weather()

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***")


    city = input("\nPlease enter a city name:\n")
    # check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city ="Lagos"

    weather_data = get_current_weather(city)
    pprint("\n")
    pprint(weather_data)
    # get_current_weather()

