import os

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

URL = "https://web.whatsapp.com"

if __name__ == "__main__":
    
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.join(os.getcwd(), "whatsapp_automation")}")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url=URL)

    search_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
    )

    search_box.clear()
    contact = "Bispo"
    search_box.send_keys(contact)

    sleep(3)

    print("ok")

    driver.quit()