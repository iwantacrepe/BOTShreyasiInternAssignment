from collections import defaultdict

def aggregate_weather_data(records):
    city_data = defaultdict(lambda: {'temperature': [], 'humidity': []})

    for record in records:
        city = record.get('city')
        if city:
            if 'temperature' in record:
                city_data[city]['temperature'].append(record['temperature'])
            if 'humidity' in record:
                city_data[city]['humidity'].append(record['humidity'])

    avg_weather = {}
    for city, data in city_data.items():
        avg_temp = sum(data['temperature']) / len(data['temperature']) if data['temperature'] else None
        avg_humidity = sum(data['humidity']) / len(data['humidity']) if data['humidity'] else None
        avg_weather[city] = {'average_temperature': avg_temp, 'average_humidity': avg_humidity}

    return avg_weather

records = [
    {'city': 'New York', 'temperature': 23, 'humidity': 60},
    {'city': 'New York', 'temperature': 25},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 50},
    {'city': 'Los Angeles', 'humidity': 55}
]

print(aggregate_weather_data(records))
