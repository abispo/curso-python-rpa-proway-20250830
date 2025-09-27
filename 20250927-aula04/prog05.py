# Setando cookies e manipulando a navegação

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )
    driver.get("https://www.proway.com.br/")

    driver.add_cookie({"name": "proway_rpa", "value": "OK"})

    cookies = driver.get_cookies()
    print(cookies)
    
    driver.get("https://www.uol.com.br")
    driver.get("https://www.google.com.br")

    # Volta para a página anterior (uol)
    driver.back()

    # Atualiza a página atual
    driver.refresh()

    # Vai pra próxima página (google)
    driver.forward()
    sleep(3)
    driver.quit()
    