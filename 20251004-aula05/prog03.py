import pyautogui

from time import sleep

# pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

if __name__ == "__main__":
    # Url usada como base: https://www.crazygames.com/game/leek-factory-tycoon
    # Exemplo de uma automação mais complexa: https://inventwithpython.com/blog/programming-a-bot-to-play-the-sushi-go-round-flash-game.html
    print("Localizando o botão")
    sleep(5)
    try:
        botao = pyautogui.locateOnScreen("cebolinha01.png", confidence=0.5)
        print(botao)

        # centralizar na imagem
        centro_botao = pyautogui.center(botao)
        for _ in range(100):
            pyautogui.click(centro_botao)
            print("Clicou!")
    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada.")

    pyautogui.dragTo(300, duration=1)