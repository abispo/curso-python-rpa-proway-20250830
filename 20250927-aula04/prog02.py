# Baixando e configurando o webdriver utilizando a biblioteca webdriver-manager

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
    print(f"Título da página: {driver.title}")
    sleep(3)
    driver.quit()
