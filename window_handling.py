# window handling
# whenever you click on particular element, if new tab gets opened,
# on that situation it is not possible to locate the elements which are in the
# new tab directly.
# In this case we have to make the controller to move to new tab in order to
# perform the operation in new tab.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\mm\driver\chromedriver.exe")
url=r"https://www.makemytrip.com/"
driver.get(url)
driver.maximize_window()
parent = driver.current_window_handle
print(parent)
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/"
                             "div[2]/div[2]/ul/li[1]/a").click()
print("clicked on first element")
childtab = driver.window_handles
print(childtab)

for handle in childtab:
    if handle!=parent: # ! = not equalsto
        driver.switch_to.window(handle)
        time.sleep(7)
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/header/"
                                     "div[2]/div/ul/li[6]/span[1]").click()
