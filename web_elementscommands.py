from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://demowebshop.tricentis.com/login"
driver.get(url)
driver.maximize_window()

time.sleep(2)
email=driver.find_element(By.XPATH,"//input[@id='Email']")
email.send_keys("hello@gmil.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("2345678")
time.sleep(2)
tags=driver.find_element(By.XPATH,"//input[@id='RememberMe']")
tags.click()
print('check box is selected')
print(tags.is_selected())
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='button-1 login-button']").click()
time.sleep(2)
pic=driver.find_element(By.XPATH,"//img[@*='Tricentis Demo Web Shop']")
print('logo is displyed')
print(pic.is_displayed())
print(pic.size)
print(pic.location)
print(pic.rect)

driver.close()
