import requests
import re
import json
from pyquery import PyQuery as pq

response = requests.get('https://www.dxy.cn/')
home_page = response.content.decode()
# soup = BeautifulSoup(home_page,'lxml')
soup = pq(home_page)
# script = soup.find(attrs={'class','breakAll Section1_link__2u9eS'})
script = soup('.Section1_link__2u9eS')
print(script.text())





            