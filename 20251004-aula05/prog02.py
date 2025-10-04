# Controle do teclado

import keyboard
import pyautogui
import datetime

from time import sleep

pyautogui.PAUSE = 1.5

if __name__ == "__main__":
    # Abrindo a janela executar do windows
    pyautogui.hotkey("win", "r")

    # Digitando notepad para ser aberto o bloco de notas
    pyautogui.write("notepad", interval=0.1)
    pyautogui.press("enter")

    sleep(2)

    # Voltando pra janela do VSCode (utilizando a lib keyboard)
    keyboard.press_and_release("alt+tab")
    
    pyautogui.moveTo(960, 540)
    pyautogui.click()

    # Utilizamos o botão de scroll do mouse
    pyautogui.scroll(1000)
    pyautogui.moveTo(200, 180)
    pyautogui.click()

    # Selecionamos o texto
    pyautogui.dragTo(960, 1080, duration=1)

    # Abaixo colamos o txto no notepad, damos um nome e salvamos
    keyboard.press_and_release("ctrl+c")
    sleep(1)
    keyboard.press_and_release("alt+tab")
    sleep(1)
    keyboard.press_and_release("ctrl+v")
    sleep
    keyboard.press_and_release("ctrl+s")
    data_hora = datetime.datetime.now(datetime.UTC).strftime(
        "%Y%m%d%H%M%S"
    )
    keyboard.write(f"{data_hora}_automation.txt", delay=0.1)
    sleep(1)
    keyboard.press_and_release("alt+l")
    sleep(1)

    # Aqui é tirado um screenshot da tela, e depois o notepad é fechado
    pyautogui.screenshot(f"{data_hora}_evidencia.png")
    sleep(1)
    keyboard.press_and_release("alt+f4")

