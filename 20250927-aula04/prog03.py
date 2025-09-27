# Localizando elementos na página

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.page_load_strategy = "eager"

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options
    )

    # Encontrando um elemento pelo id
    driver.get("https://www.proway.com.br/")

    # Espera ímplicita
    driver.implicitly_wait(3)

    text_busca = driver.find_element(By.ID, "termoBuscaCurso")
    sleep(1)
    text_busca.send_keys("Python")
    text_busca.send_keys(Keys.ENTER)

    # Espera explícita
    link_moda_textil = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Moda e Têxtil"))
    )

    link_moda_textil.click()
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "listaCursos"))
    )

    cursos_moda_textil = driver.find_elements(By.XPATH, "//div[@class='sombra']//h2")
    print("=== Cursos na área de Moda e Têxtil ===")

    for curso in cursos_moda_textil:
        print(f"* {curso.text}.")

    driver.quit()