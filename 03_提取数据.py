import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.runoob.com/w3cnote/python-pip-install-usage.html')
home_page = response.content.decode()
# print(home_page)

soup = BeautifulSoup(home_page,'lxml')
text = soup.find(attrs={"class":"sidebar-box cate-list"})
print(text)