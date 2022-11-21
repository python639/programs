from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://www.facebook.com/login/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//button[contains(text(),'Log')]").click()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,"//a[contains(text(),'Forgotten account?')]").click()
time.sleep(2)
driver.back()
driver.quit()