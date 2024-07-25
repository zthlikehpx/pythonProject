import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
hero = input("输入英雄")
position = input("输入位置")
url = f'https://www.op.gg/champions/{hero}/counters/{position}'
driver = webdriver.Firefox()
driver.get(url)


# 反制
buttons = driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/aside/div[1]/div[2]/table/tbody')

# /html/body/div[1]/div[7]/div/aside/div[1]/div[2]/table/tbody
# /html/body/div[1]/div[7]/div/aside/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div
# percent = driver.find_elements(By.XPATH,button+'/tr[1]')

trs = buttons.find_elements(By.TAG_NAME,'tr')
for tr in trs:
    tds = tr.find_elements(By.TAG_NAME, 'td')
    button = tds[0]
    button.click()
    name = tds[1]
    percent = driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/main/div[1]/ul/li[1]/div/div/div[1]/div')
    winrate = driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/main/div[1]/ul/li[7]/div/div/div[1]/div')
    print(name.text,percent.text,winrate.text)
# print(buttons.text)
# winrate = driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/main/div[1]/ul/li[7]/div/div/div[1]/div')


# print(button.text,percent.text,winrate.text)