import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.set_page_load_timeout(30)

driver.get("https://testindulekha.myshopify.com/")
driver.maximize_window()

driver.find_element(By.ID, "password").send_keys("testindu")
time.sleep(5)

driver.find_element(By.TAG_NAME, "BUTTON").click()
time.sleep(5)

#initialize an incremental scroll
action = ActionChains(driver)

while True:
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(5)

    add_to_cart = driver.find_element(By.XPATH, "/html/body/main/section[5]/div/div[2]/main/div[1]/button")
    if add_to_cart.is_displayed():
        action.move_to_element(add_to_cart).perform()
        add_to_cart.click()
        time.sleep(5)
        break

time.sleep(10)
driver.quit()

