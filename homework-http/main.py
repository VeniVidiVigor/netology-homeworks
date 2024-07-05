import requests
from pprint import pprint


def get_the_smartest_superhero():
    base_url = 'https://akabab.github.io/superhero-api/api'
    the_smartest_superhero = ''
    response = requests.get()
    pprint(response.json())
    # ваш код здесь
    # return the_smartest_superhero
#

pprint(get_the_smartest_superhero())
