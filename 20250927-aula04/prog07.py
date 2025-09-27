# Utilizando modo headless e tirando screenshots
import os

from datetime import datetime
from time import sleep

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
ua = UserAgent()

prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)

# No modo headless, o navegador não é aberto na tela.
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")

# Quando utilizamos o modo headless, é uma boa prática definirmos qual será o User-Agent, do contrário sistemas de detecção de bots podem bloquear o seu script
options.add_argument(f"--user-agent={ua.random}")

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options
    )

    # Encontrando um elemento pelo id
    driver.get("https://www.saucedemo.com/")

    sleep(1)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    sleep(1)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    sleep(1)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    sleep(1)

    backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_button.click()

    bike_light_element = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    bike_light_element.click()

    tshirt_element = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_element.click()

    sleep(1)

    driver.find_element(By.ID, "shopping_cart_container").click()

    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    filename = f"{datetime.now().strftime("%Y%m%d%H%M%S.png")}"
    filepath = os.path.join(screenshots_dir, filename)

    os.makedirs(screenshots_dir, exist_ok=True)

    driver.save_screenshot(filepath)