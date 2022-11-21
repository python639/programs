from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #uppercase 'S' (Select class)
import time
driver = webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url = r"C:\Users\HP\PycharmProjects\selenium\HTML\standard_listbox.html"
driver.get(url)
driver.maximize_window()

#for Dropdown
dropdwon = driver.find_element(By.ID,"standard_cars")
select = Select(dropdwon)  #uppercase 'S'--> [Select(dropdown)]
time.sleep(2)
select.select_by_value("6")  #1st method
time.sleep(2)
select.select_by_visible_text("Mercedes")    #2nd method
time.sleep(2)
select.select_by_index(1)     #3rd method

#for Listbox
listbox = driver.find_element(By.ID,"multiple_cars")
select = Select(listbox)
time.sleep(2)
select.select_by_value("11")   #1st method
time.sleep(2)
select.select_by_visible_text("Mercedes")   #2nd method
time.sleep(2)
select.select_by_index(4)      #3rd method
print(select.is_multiple)

# #for dropdown(currency)
# currency = driver.find_element(By.NAME,"currency")
# select = Select(currency)
# time.sleep(2)
# select.select_by_value("JPN")   #1st method
# time.sleep(2)
# select.select_by_visible_text("US Dollars")   #2nd method
# time.sleep(2)
# select.select_by_index(1)     #3rd method