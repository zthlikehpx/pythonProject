from selenium import webdriver
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq

driver = webdriver.Firefox()
html = driver.get('https://lol.qq.com/main.shtml')
doc = pq(html)
print(doc)