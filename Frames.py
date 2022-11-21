from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"C:\Users\HP\PycharmProjects\selenium\HTML\frames.html"
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(10)
driver.switch_to.frame("frame2")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"About Selenium").click()
time.sleep(2)
driver.close()
