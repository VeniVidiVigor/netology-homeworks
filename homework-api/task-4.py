import requests


def find_uk_city(coordinates: list) -> str:
    UK_CITIES = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    params = {
        'format': 'json',
        'lat': '',
        'lon': ''
    }
    for lat, lon in coordinates:
        params['lat'] = lat
        params['lon'] = lon
        url = f'https://geocode.maps.co/reverse?'
        """Ваш код здесь"""
        response = requests.get(url, params=params)
        for cities in UK_CITIES:
            if response.json()['address']['city'] == cities:
                city = response.json()['address']['city']
                return city


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
