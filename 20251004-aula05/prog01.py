# Controle básico do mouse

import pyautogui

pyautogui.PAUSE = 1.5

if __name__ == "__main__":
    # Pegar o tamanho atual da tela
    altura_tela, largura_tela = pyautogui.size()
    print(f"Altura da tela: {altura_tela}")
    print(f"Largura da tela: {largura_tela}")

    # Pegar posição atual do mouse
    eixo_x_mouse, eixo_y_mouse = pyautogui.position()
    print(f"Posição X do mouse: {eixo_x_mouse}")
    print(f"Posição Y do mouse: {eixo_y_mouse}")

    # Cliques do mouse
    print("Movendo o mouse e clicando")
    pyautogui.moveTo(960, 540, 1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.click(x=150, y=600)
    pyautogui.doubleClick(960, 25, 2)
    pyautogui.rightClick(960, 540, duration=1, tween=pyautogui.easeInOutElastic)

    # Drag'n drop
    print("Movendo mouse usando posição relativa")
    pyautogui.moveRel(-600, -300, duration=1)
    pyautogui.press("esc")
    pyautogui.dragTo(400, 700, duration=1)
