from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(r"C:\Users\HP\PycharmProjects\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = r""
