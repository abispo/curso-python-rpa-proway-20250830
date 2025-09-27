# Trabalhando com abas e janelas

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.window import WindowTypes
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )
    driver.get("https://www.proway.com.br/")
    print(f"URL atual: {driver.current_url}")

    # Aqui pegamos o ID da janela atual, ou seja, onde foi aberto o site da proway
    # O atributo windows_handles do objeto driver, armazena uma lista com os ids das janelas
    main_window_handler = driver.current_window_handle

    sleep(2)

    # O método new_window cria uma nova janela do tipo especificado. No caso abaixo, será criada uma aba
    # Caso quiséssemos criar uma nova janela, usaríamos WindowsTypes.Window
    # Quando mudamos pra outra janela, todos os comandos do selenium serão aplicados nessa janela atual.
    # Ou seja, o ID de current_window_handle e definido como essa janela atual
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get("https://www.github.com")
    print(f"URL atual: {driver.current_url}")

    sleep(2)

    # Abaixo estamos novamente trocando de janela, nesse caso voltando pra primeira janela criada.
    driver.switch_to.window(main_window_handler)

    # Se quisermos, podemos utilizar javascript para abrir uma nova página
    driver.execute_script("window.open('https://www.uol.com.br', '_blank');")

    print(driver.title)

    driver.quit()