from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gclid=CjwKCAjwp9qZBhBkEiwAsYFsbxDPm8gFckr-aF-0Is_9yMINcdq137LXffCdCdmWJwXcR1E-nvtrpxoCs7YQAvD_BwE&gclsrc=aw.ds"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("python")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("python95134@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("9513@123")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mobile']").send_keys("9513419428")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div/div/div[1]/form/div[2]/div[4]/div[2]/div[2]/div[2]/h2").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='currentCity']").send_keys("ben")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='sa-dd-scrollcurrentCity']/div[1]/ul/li[1]/span/span[3]").click()
time.sleep(2)
abc = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div/div/div[1]/form/div[2]/div[6]/div[1]/div[1]/button").click()
time.sleep(2)
abc
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div/div/div[1]/form/div[2]/div[8]/button").click()
time.sleep(2)
# driver.close()