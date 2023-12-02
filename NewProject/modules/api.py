import requests
api_key =  "336633f9d31fd19a2d94570ca76d354f"

def temper(kelvin: float):
    return str(int(kelvin - 273.15))
def get_data_weth(city = "Dnipro"):
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url_api)
    if response.status_code == 200:
        return response.json()
    else:
        print(response)
print(get_data_weth()['weather'][0]['main'])