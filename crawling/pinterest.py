from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

import os
from urllib import request
import sys


def login():
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button').send_keys(Keys.ENTER)

    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="email"]').send_keys('liruien3430@naver.com')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('ssho2323')

    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/form/div[5]/button').send_keys(Keys.ENTER)

    driver.implicitly_wait(10)

def search(key = None):
    s = driver.find_element_by_xpath('//*[@id="searchBoxContainer"]/div/div/div[2]/input')
    s.send_keys(key)
    s.send_keys(Keys.ENTER)

# scroll down page
def scroll(driver, urls):
    # last_height = driver.execute_script("return document.body.scrollHeight")
    num_page_down = 50
    body = driver.find_element_by_tag_name('body')
    while num_page_down:
        print("num_page_down {} times left".format(num_page_down))
        urls = get_url(driver, urls)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_page_down-=1
    time.sleep(5)
    return urls

def get_url(driver, urls):
    html = driver.page_source
    soup = bs(html, 'html.parser')
    images = soup.findAll('img')
    file_num = 0
    for line in images:
        if str(line).find('src') != -1 and str(line).find('http') < 100:
            # print(file_num, " : ", line['src'])
            print(str(line['src']))
            print(type(str(line['src'])))
            urls.append(str(line['src']))
            file_num += 1
    return urls

# 1차적으로 웹상에서 검색어를 입력해보면서 적절한 검색어를 선정하면 좋을
if __name__ == "__main__":
    driver = webdriver.Chrome('/home/yeeunlee/ssho/ssho-item-tagging-api/crawling/chromedriver')
    driver.get("http://www.pinterest.co.kr")
    # 로그인 우회 코드 추가(?)
    login()
    key = input("input keyword : ")
    time.sleep(random.uniform(1, 4))
    search(key)
    time.sleep(random.uniform(1, 4))
    urls = []
    # default scroll num = 50
    # 1. 변수지정
    urls = scroll(driver, urls)
    df = pd.DataFrame(urls)
    print(df.head())
    # csv저장
    df.to_csv(key+'.csv')

    # driver.implicitly_wait(5)




