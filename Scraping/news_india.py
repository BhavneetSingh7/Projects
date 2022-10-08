from bs4 import BeautifulSoup
import requests

def sum_string(x):
    val = ''
    for e in x:
        val = val + e + ' '
    if val[0] == '  ':
        return val[1:]
    return val

res = requests.get('https://www.india.com/')
soup = BeautifulSoup(res.text,'html.parser')

aside = soup.select('aside.iwpl-lg-4')
l = aside[0].find_all('li')

for i in range(len(l)):
    c = l[i].a.get_text()
    c = c.split(' ')
    print(str(i+1)+' :: ',sum_string(c[16:-29]))