import requests
import json
city = input("Enter the name of the city that you want to check weather: ")

url = f"https://api.weatherapi.com/v1/current.json?key=b5a9a15838254c36a6534115232008&q={city}"
req = requests.get(url)
# print(req.text)
weatherDic = json.loads(req.text)
weather = weatherDic['current']['temp_c']
print(weatherDic['current']['temp_c'])
print(f'The current weather in {city} is {weather} degrees')
