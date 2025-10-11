import datetime
import os

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

URL = "https://web.whatsapp.com"

if __name__ == "__main__":
    
    # Utiizamos a pasta de usuário para não ser necessário ler o QR Code todas as vezes
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.join(os.getcwd(), "whatsapp_automation")}")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url=URL)

    # Aqui procuramos pela barra de pesquisa de contato
    search_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
    )

    search_box.clear()
    contact_name = "Bispo"
    search_box.send_keys(contact_name)

    sleep(3)

    # # Clicamos no contato
    driver.find_element(By.XPATH, f"//span[@title='{contact_name}']").click()

    # Busca pela última mensagem enviada
    # last_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-in')]")
    # actions = ActionChains(driver)
    # actions.move_to_element(last_message).perform()
    # sleep(2)

    # Response a mensagem
    # reply_button = driver.find_element(By.XPATH, )

    # # Enviar mensagem
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
    message_box.send_keys(f"Mensagem automática: {datetime.datetime.now(datetime.UTC).strftime("%d/%m/%Y %H:%M:%S")}")
    message_box.send_keys(Keys.ENTER)

    sleep(3)


    driver.quit()