# Baixando e configurando o webdriver manualmente

import os

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
service = ChromeService(executable_path=os.path.join(os.getcwd(), "chromedriver.exe"))

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=service, options=options
    )

    driver.get("https://www.proway.com.br/")
    print(f"Título da página: {driver.title}")
    sleep(3)
    driver.quit()
