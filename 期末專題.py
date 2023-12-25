#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# In[2]:


username = input('請輸入你的帳號：')
password = input('請輸入你的密碼：')
kword = input('請輸入你想找的關鍵詞：')


# In[3]:


path = r'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe' 
service=Service(executable_path=path)
service


# In[4]:


chrome=webdriver.Chrome(service=service)
chrome.get('https://mbasic.facebook.com')
time.sleep(5)


# In[5]:


un_xpath = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[1]/input'
un_element = chrome.find_element(By.XPATH, un_xpath)
un_element


# In[6]:


un_element.send_keys(username)


# In[7]:


pw_xpath='/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[2]/section/input'

pw_element = chrome.find_element(By.XPATH, pw_xpath)
pw_element


# In[8]:


pw_element.send_keys(password)


# In[9]:


input_xpath = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[3]/input'
input_button = chrome.find_element(By.XPATH, input_xpath)
input_button.click()


# In[10]:


chrome.get('https://mbasic.facebook.com')


# In[11]:


kw_xpath = '/html/body/div/div/div[1]/div/form/table/tbody/tr/td[2]/input'
kw_element = chrome.find_element(By.XPATH, kw_xpath)
kw_element


# In[12]:


kw_element.send_keys(kword)


# In[13]:


kwb_xpath = '/html/body/div/div/div[1]/div/form/table/tbody/tr/td[3]/input'
kw_button = chrome.find_element(By.XPATH, kwb_xpath)
kw_button.click()


# In[15]:


for x in range(3):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5)


# In[3]:


titles = soup.find_all(
    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        for post in posts:
            print(post.text)

    print("-" * 30)


# In[ ]:




