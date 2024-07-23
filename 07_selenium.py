from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
 
driver = webdriver.Edge()

driver.get('https://www.csdn.net')
sleep(2)
driver.get('https://blog.csdn.net/weixin_74435164?spm=1000.2115.3001.5343')
sleep(2)
driver.back()
sleep(2)
driver.forward()

# driver.find_element_by_id('blogHuaweiyunAdvert')
