import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

os.environ['PATH'] += r";C:/webdrivers"
chr_options = Options()
chr_options.headless = True
driver = webdriver.Chrome(options=chr_options)
driver.get("https://www.google.com/search?q=News&hl=en")

headlines = driver.find_elements(By.CLASS_NAME,'mCBkyc')
headlines_links = driver.find_elements(By.CSS_SELECTOR, 'a[jsname="YKoRaf"]')

def get_news_txt():
    with open('news.txt','w',encoding="utf-8") as f:
        for i in range(len(headlines)):
            f.write(str(i+1)+' :: '+headlines[i].text + '\n' +headlines_links[i].get_attribute('href'))
            f.write('\n')

outer = [
    """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News</title>
</head>
<body>""",
"""</body>
</html>
"""
]
def get_news_html():
    with open('news.html','w',encoding="utf-8") as f:
        f.write(outer[0])
        for i in range(len(headlines)):
            f.write('<p>'+'<a href="'+headlines_links[i].get_attribute('href')+'" >'+str(i+1)+' :: '+headlines[i].text + '\n'+'</a></p>')
            f.write('\n')
        f.write(outer[1])

if __name__ == '__main__':
    get_news_html()
    # get_news_txt()