from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"http://demowebshop.tricentis.com/login"
driver.get(url)
driver.maximize_window()

links=driver.find_elements(By.XPATH,"//a")
print(len(links))

for i in links:
    URL=i.get_attribute("href")
    print(URL)
    print(i.text)
driver.close()
