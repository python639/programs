from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url="file:///D:/SELENIUM/Chrome%20files/axes%20function.html"
driver.get(url)
driver.maximize_window()

#to doubble click on element
ab=driver.find_element(By.CSS_SELECTOR,"a[class='listLink']")
action=ActionChains(driver)
action.pause(2)        #pause action chain
action.double_click(ab).perform()
time.sleep(3)

#to right click on element
cd=driver.find_element(By.CSS_SELECTOR,"a[class='listLink']")
action.context_click(cd).perform()

