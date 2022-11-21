from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url = r"https://www.facebook.com/login/"
driver.get(url)
driver.maximize_window()

time.sleep(2)
driver.find_element(By.ID, "email").send_keys("rahul@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "pass").send_keys("9874563214")
time.sleep(2)
driver.find_element(By.ID, "loginbutton").click()
driver.close()