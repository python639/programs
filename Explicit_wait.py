from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #aliasing

driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"C:\Users\HP\PycharmProjects\selenium\HTML\loading.html"
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(20)
wait=WebDriverWait(driver,30)
wait.until(EC.title_is("pyspiders"))   #condition for checikng the title
wait.until(EC.url_contains("ers/HP/PycharmProjects/selenium/HTML/loading.html"))   #condition for url contains

driver.find_element(By.NAME,"fname").send_keys("sandya")
driver.find_element(By.NAME,"lname").send_keys("123456")

