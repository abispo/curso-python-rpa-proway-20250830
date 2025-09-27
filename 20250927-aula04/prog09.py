# Perfis de navegação
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

os.makedirs("data_dir", exist_ok=True)
os.makedirs("Default", exist_ok=True)

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(f"--user-data-dir={os.path.join(os.getcwd(), "data_dir")}")
options.add_argument(f"--profile-directory={os.path.join(os.getcwd(), "Proway")}")

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.get("https://www.proway.com.br")
    # driver.get("https://www.uol.com.br")
    # driver.get("https://www.google.com.br")
    sleep(5)
    driver.quit()