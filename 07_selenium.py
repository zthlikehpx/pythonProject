from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get('https://www.baidu.com/')
el = driver.find_element(By.ID, 'kw')
el.send_keys('腾讯\n')

# 等待搜索按钮出现并点击
su = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'su'))
)
su.click()

# 等待搜索结果中的第一个链接出现并点击
a = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[3]/div[1]/div/div[1]/h3/a[1]'))
)
a.click()
