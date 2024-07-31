from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

text = input('输入你想翻译的内容:')
# print('内容', text)
url = webdriver.Firefox()
url.get('https://fanyi.baidu.com')

content = WebDriverWait(url,10).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/div'))
)
# 切片
content.send_keys(text)

answer = WebDriverWait(url,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="trans-selection"]'))
)
print(answer.text)