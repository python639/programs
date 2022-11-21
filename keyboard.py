from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://www.facebook.com/login/"
driver.get(url)
driver.maximize_window()

username=driver.find_element(By.ID,"email")
time.sleep(2)
username.send_keys("Admin")
username.send_keys(Keys.CONTROL+'a')
time.sleep(2)
username.send_keys(Keys.CONTROL+'c')
time.sleep(2)
password=driver.find_element(By.ID,"pass")
password.send_keys(Keys.CONTROL+'v')
time.sleep(2)
login=driver.find_element(By.ID,"loginbutton")
login.send_keys(Keys.ENTER)

#to delete
#password.send_keys(Keys.CONTROL+'a')
#password.send_keys(Keys.DELETE)

#delete using back_space
# count=len(password.get_attribute("value"))
# for i in range(count+1):
#     password.send_keys(Keys.BACK_SPACE)
#     time.sleep(1)
# time.sleep(5)
