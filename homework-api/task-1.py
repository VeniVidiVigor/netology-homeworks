import requests


def get_the_smartest_superhero():
    the_smartest_superhero = ''
    max_intelligence = 0
    base_url = 'https://akabab.github.io/superhero-api/api/'
    heroes = ['Hulk', 'Captain America', 'Thanos']
    response = requests.get(base_url + 'all.json')
    new_list = []
    for hero in response.json():
        if hero['name'] in heroes:
            new_list.append(hero)
        if hero['powerstats']['intelligence'] > max_intelligence:
            max_intelligence = hero['powerstats']['intelligence']
            the_smartest_superhero = hero['name']
    return the_smartest_superhero


get_the_smartest_superhero()

