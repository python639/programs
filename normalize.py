from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://www.facebook.com/login/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//input[normalize-space(@class)='inputtext _55r1 inputtext _1kbt inputtext _1kbt']").send_keys("123")
driver.find_element(By.XPATH,"//button[normalize-space(@class)='_42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy']").click()
'''time.sleep(2)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH,"//a[text()='Sign up for Facebook']").click()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,"//button[@id='loginbutton']").click()
driver.back()'''
