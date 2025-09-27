# Action chains

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument("--start-maximized")

if __name__ == "__main__":
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options
    )

    actions = ActionChains(driver)
    # Encontrando um elemento pelo id
    driver.get("https://demoqa.com/menu")

    menu_item = driver.find_element(By.LINK_TEXT, "Main Item 2")
    actions.move_to_element(menu_item).perform()
    sleep(5)
    actions.move_to_element(driver.find_element(By.LINK_TEXT, "SUB SUB LIST »")).perform()

    sleep(2)

    driver.get("https://demoqa.com/droppable")

    sleep(3)

    drag_item = driver.find_element(By.ID, "draggable")
    drop_item = driver.find_element(By.ID, "droppable")

    actions.drag_and_drop_by_offset(drag_item, -100, 50).perform()
    sleep(2)
    actions.drag_and_drop(drag_item, drop_item).perform()
    
    drop_item_content = drop_item.find_element(By.TAG_NAME, 'p')
    assert drop_item_content.text == "Dropped!"

    driver.quit()