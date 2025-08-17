import requests

def get_weather(city):
    api_url = f"https://wttr.in/{city}?format=3"
    response = requests.get(api_url)
    return response.text

if __name__ == "__main__":
    print(get_weather("London"))
