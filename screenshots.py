from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://www.facebook.com/login.php/"
driver.get(url)
driver.maximize_window()

#screenshot after login
driver.save_screenshot(r"C:\Users\HP\PycharmProjects\selenium\screenshots\beforelogin.png")
time.sleep(2)
driver.find_element(By.ID,"email").send_keys("abd")
time.sleep(2)
driver.find_element(By.ID,"pass").send_keys("123")
time.sleep(2)
driver.find_element(By.NAME,"login").click()
time.sleep(2)
#screenshot after login
driver.get_screenshot_as_file(r"C:\Users\HP\PycharmProjects\selenium\screenshots\afterlogin.png")
time.sleep(2)
driver.get_screenshot_as_png()
time.sleep(2)
driver.close()