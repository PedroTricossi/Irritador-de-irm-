import pyautogui as pg
import time
import pega_frase

time.sleep(5)

def envia_mensagem(n):
    for i in range(n):
        frase_aleatoria = pega_frase.request()
        
        anime = pega_frase.anime(frase_aleatoria)
        personagem = pega_frase.personagem(frase_aleatoria)
        frase = pega_frase.frase(frase_aleatoria)

        pg.typewrite(f'No iconico anime "{anime}", um sabio personagem chamado "{personagem}", uma vez disse: "{frase}"')

        time.sleep(0.5)
        pg.press('enter')

envia_mensagem(5)