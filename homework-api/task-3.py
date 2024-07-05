import requests

token = 'dict.1.1.20230919T180204Z.ccb28542d640ec63.726fe168f183ba44be3504546542e3cab6afbcba'


def translate_word(word):
    all_mean_words = []
    url = f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={token}&lang=ru-en&text={word}'
    response = requests.get(url)
    for x in response.json()['def']:
        for i in x['tr']:
            all_mean_words.append(i['text'])
            trans_word = all_mean_words[0]
    return trans_word


print(translate_word(input()))
# if __name__ == '__main__':
#     word = 'машина'
#     assert translate_word(word) == 'car'
