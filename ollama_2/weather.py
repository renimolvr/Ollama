import requests

def get_weather(city):
    """
    Fetches weather information for a given city using the wttr.in API.

    Args:
        city (str): Name of the city.

    Returns:
        str: Weather condition and temperature.
    """
    url = f"https://wttr.in/{city}?format=%C+%t"  # Fetch only condition and temperature
    response = requests.get(url)

    if response.status_code == 200:
        return f"Weather in {city}: {response.text.strip()}"
    else:
        return "Could not fetch weather data."

# Example usage
if __name__ == "__main__":
    city_name = input("Enter city name: ")  # User inputs the city
    print(get_weather(city_name))

