import json
import requests

def request():
    r = requests.get('https://animechan.vercel.app/api/random')

    return r

def anime(anime):

    return anime.json()["anime"]

def personagem(anime):

    return anime.json()["character"]

def frase(anime):

    return anime.json()["quote"]

