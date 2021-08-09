import pyautogui as pg
import time
import frase_anime

time.sleep(5)

def envia_mensagem(n):
    for i in range(n):
        frase_aleatoria = frase_anime.request()
        
        anime = frase_anime.anime(frase_aleatoria)
        personagem = frase_anime.personagem(frase_aleatoria)
        frase = frase_anime.frase(frase_aleatoria)

        pg.typewrite(f'Cara irmã, você sabia que no iconico anime "{anime}", um sabio personagem chamado "{personagem}", uma vez disse: "{frase}"')

        time.sleep(0.5)
        pg.press('enter')