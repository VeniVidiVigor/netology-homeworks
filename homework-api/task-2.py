import requests


def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ''
    max_intelligence = 0
    base_url = 'https://akabab.github.io/superhero-api/api/'
    response = requests.get(base_url + 'all.json')
    # ваш код здесь
    for hero in response.json():
        for ids in superheros:
            if ids == hero['id']:
                if hero['powerstats']['intelligence'] > max_intelligence:
                    max_intelligence = hero['powerstats']['intelligence']
                    the_smartest_superhero = hero['name']
    return the_smartest_superhero


if __name__ == '__main__':
    assert get_the_smartest_superhero([332, 149, 655]) == 'Thanos'
