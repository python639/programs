from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"C:\Users\HP\PycharmProjects\selenium\HTML\con_alert.html"
driver.get(url)
driver.maximize_window()

#for confirmation alert
#for dissmiss
time.sleep(3)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(3)

driver.refresh()

#for accepting
time.sleep(3)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()