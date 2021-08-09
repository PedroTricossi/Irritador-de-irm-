import pyautogui as pg
import time
import fato_dog

time.sleep(5)

def envia_mensagem(n):
    for i in range(n):
        fato_aleatorio = fato_dog.fato(1)

        pg.typewrite(f'Dear sister, did you know that interesting fact about dogs is: "{fato_aleatorio}"')

        time.sleep(0.5)
        pg.press('enter')