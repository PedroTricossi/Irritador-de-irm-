import json
import requests

def request(i):
    r = requests.get(f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number={i}')

    return r

def fato(i):

    fato = request(i)
    
    return fato.json()[0]['fact']