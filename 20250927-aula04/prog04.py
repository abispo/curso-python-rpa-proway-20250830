# Trabalhando com iframes

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.page_load_strategy = "eager"

def show_page_text(driver: webdriver.Chrome):
    div_geral = driver.find_element(By.XPATH, "//h1[@class='text-center']/following-sibling::div")
    print(f"Texto da página: {div_geral.text}")

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options
    )

    print('='*30)

    # Encontrando um elemento pelo id
    driver.get("https://demoqa.com/frames")
    driver.implicitly_wait(5)

    show_page_text(driver)

    try:
        texto = driver.find_element(By.ID, "sampleHeading")
    except NoSuchElementException:
        print("O elemento não foi encontrado pois está dentro de um iframe.")

    iframe1 = driver.find_element(By.ID, "frame1")
    
    # Aqui definimos o conteúdo atual como o conteúdo que está dentro do iframe. Todas as buscas serão feitas dentro dele
    driver.switch_to.frame(iframe1)

    elemento_h2 = driver.find_element(By.ID, "sampleHeading")
    print(f"O texto do elemento h2 dentro do iframe é '{elemento_h2.text}'")

    try:
        show_page_text(driver)
    except NoSuchElementException:
        print("Precisamos definir o conteúdo da página como padrão para podermos pesquisar os itens novamente.")

    driver.switch_to.default_content()
    show_page_text(driver)