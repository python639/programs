from selenium import webdriver
import time
driver=webdriver.Chrome(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
url=r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# to add the cookie
Cookie={'name':'mycookie', 'value':'pyspiders'}
driver.add_cookie(Cookie)
time.sleep(3)
print(Cookie,'cookies is added')

#to get cookie with specific name
Cookie=driver.get_cookie('mycookie')
print(Cookie)

#to get all the cookies from web page
allcookies=driver.get_cookies()
print(allcookies)

# to delete the specific cookie
driver.delete_cookie('mycookie')
print('cookie is deleted')

#to delete all the cookies
deleting=driver.delete_all_cookies()
print(deleting, 'deleted all the cookies')

# after deleting it returns empty lsit
proof=driver.get_cookies()
print(proof)