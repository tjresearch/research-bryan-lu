import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from requests import Session
from bs4 import BeautifulSoup
import json


def make_ascii(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        removed = ""
        for ch in s:
            if ord(ch) >= 128:
                continue
            removed += ch
        return removed  # string is not ascii
    else:
        return s  # string is ascii

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:/Users/bryan/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)
#scrollbar = driver.find_element_by_class_name('aops-scroll-inner')
#ActionChains(driver).move_to_element(scrollbar) # Figure out how to force the scroll bar to scroll, otherwise, we'll hack it
#lenOfPage = driver.execute_script("window.scrollTo(0, document.body.div.div.div.div.div.div.div.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#match = False
now = time.time()

session = Session()
#session.head('https://artofproblemsolving.com/community/c6t48f6_geometry')
headers = {'Host': 'artofproblemsolving.com', 'Connection': 'keep-alive', 'Content-Length': '236',
           'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
           'Sec-Fetch-Mode': 'cors', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Sec-Fetch-Site': 'same-origin',
           'Referer': 'https://artofproblemsolving.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9',
           'Cookie': '_ga=GA1.2.193132615.1527439590; _fbp=fb.1.1549664474250.1900488494; __cfduid=db80d581ae3c0b5b0a3ca0d9b4d0699e31558997043; _gcl_au=1.1.1506193588.1560704187; _hjid=6a211d36-a51c-44dc-adb1-15aabcef0373; aopsuid=1; aopssid=1oNwSXnepHEf156829878800212UVaqoZePRX7; _gid=GA1.2.1995018911.1568298790; cmty_init_time=1568302609'}

payload = {'category_type': 'forum', 'log_visit': 0, 'required_tag': '6_48', 'fetch_before': '1568259383', 'user_id': 0,
           'fetch_archived': 0, 'fetch_announcements': 0, 'category_id': 6, 'a': 'fetch_topics',
           'aops_logged_in': 'false', 'aops_user_id': 1, 'aops_session_id': '2cac80da98c2d69cb2b07d4dbb545505'}
#session.get('https://artofproblemsolving.com/community/c6t48f6_geometry', headers=headers)

while time.time() - now < 60: #and match == False:
    #lastCount = lenOfPage
    #ActionChains(driver).send_keys(u'\ue015')
    #session.get('https://artofproblemsolving.com/community/c6t48f6_geometry', data=payload, headers=headers)

    response = session.post('https://artofproblemsolving.com/community/c6t48f6_geometry', data=payload, headers=headers)

    time.sleep(3)
    #lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    #if lastCount == lenOfPage:
        #match = True

page = session.get('https://artofproblemsolving.com/community/c6t48f6_geometry')
driver.get("https://artofproblemsolving.com/community/c6t48f6_geometry")
pageSource = driver.page_source
soup = BeautifulSoup(page, 'lxml')
#soup = BeautifulSoup(pageSource, 'lxml')
tempDriver = webdriver.Chrome("C:/Users/bryan/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)
urlfile = open("urlfile.txt", "w+")
newProbFile = open("newProbs.txt", "w+")
allProbTabs = soup.find_all('a', class_='cmty-full-cell-link')
for probTab in allProbTabs[2::3]:
    if probTab["href"] == "/community/c6_high_school_olympiads":
        continue
    link = "https://artofproblemsolving.com" + probTab["href"]
    tempDriver.get(link)
    time.sleep(1)
    postPage = tempDriver.page_source
    threadsoup = BeautifulSoup(postPage, 'lxml')
    allResps = threadsoup.find_all("div", class_='cmty-post-html')
    op = allResps[0]
    currentprob = ""
    for itm in op.contents:
        if issubclass(type(itm), str):
            currentprob += itm
        elif itm.name == "div":
            continue
        elif itm.name == "img":
                currentprob += itm['alt']
        elif itm.name == "span":
            for piece in itm.contents:
                if issubclass(type(piece), str):
                    currentprob += piece
                else:
                    currentprob += piece['alt']
    currentprob += '\n'
    newProbFile.write(make_ascii(currentprob))
    urlfile.write(link + "\n")

urlfile.close()
newProbFile.close()


