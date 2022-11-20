from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
def login_page():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.find_element(By.NAME,"username").send_keys("Admin")
    time.sleep(10)
    driver.find_element(By.NAME,"password").send_keys("admin123")
    time.sleep(10)
    driver.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
    time.sleep(10)
    message ="Invalid credentials"
    error = driver.find_element(By.XPATH,"//p[text()='Invalid credentials']")
    if any(message in e.text for e in error):
        print("Login failed")
    else:
        print("Login success")

login_page()




