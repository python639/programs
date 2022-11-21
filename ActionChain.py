from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url="https://www.flipkart.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
action=ActionChains(driver)
electonics=driver.find_element(By.XPATH,"//div[text()='Electronics']")
action.move_to_element(electonics)
action.perform()


audio=driver.find_element(By.XPATH,"//a[text()='Audio']")
action.move_to_element(audio)
action.perform()

headphones=driver.find_element(By.XPATH,"//a[text()='Wired Headphones']")
action.move_to_element(headphones)
action.click().perform()

boat=driver.find_element(By.XPATH,"//a[text()='boAt Bassheads 100 Wired Headset']")
action.move_to_element(boat)
action.click().perform()

#adding to cart
add=driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
action.move_to_element(add)
action.click().perform()
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()