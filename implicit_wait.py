from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"C:\Users\HP\PycharmProjects\selenium\HTML\loading.html"
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(30)
driver.find_element(By.NAME,"fname").send_keys("SHIVA")
time.sleep(2)
driver.find_element(By.NAME,"lname").send_keys("123456")
driver.find_element(By.NAME,"login").click()
