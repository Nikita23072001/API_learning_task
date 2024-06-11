import requests
import csv

# Parametry żądania
city = "Cracow"
api_key = "805bac77baa6a0265fdd0421cfd134b3"  # Uzupełnij własnym kluczem API
api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# Wykonanie żądania GET do API
response = requests.get(api_url)
data = response.json()

# Wyodrębnienie potrzebnych danych z prognozy (lista prognoz co 3 godziny na 5 dni)
forecast_list = data.get('list', [])

# Przechowywanie przetworzonych danych
weather_data = []
for forecast in forecast_list:
    weather_data.append([
        forecast.get('dt_txt', 'No Date'),
        forecast.get('main', {}).get('temp', 'No Temperature'),
        forecast.get('main', {}).get('humidity', 'No Humidity'),
        forecast.get('weather', [{}])[0].get('description', 'No Description')
    ])

# Nazwa pliku CSV
csv_file = 'weather_forecast.csv'

# Zapis danych do pliku CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Temperature (C)', 'Humidity (%)', 'Weather Description'])  # Nagłówki kolumn
    writer.writerows(weather_data)

print(f"Dane zostały zapisane do {csv_file}")