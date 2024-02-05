#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install selenium


# In[1]:


from selenium import webdriver


# In[2]:


from time import sleep


# In[3]:


from selenium.webdriver.common.by import By


# In[4]:


val=str(input("Enter Name of artist and song"))


# In[10]:


def runner():
    
    browser=webdriver.Chrome()
    browser.get("https://www.ultimate-guitar.com/")
    browser.maximize_window()
    sleep(5)
    button=browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/p[2]/form/button")
    searchbar=browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/p[2]/form/div/input")
    searchbar.send_keys(val2)
    sleep(2)
    button.click()
    tabbutton=browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/section/nav/div[1]/nav/a[3]')
    tabbutton.click()
    linktotabs=browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/section/article/div/div[6]/div[2]/header/span/span/a/span/span[5]/b')
    linktotabs.click()
    tuning=browser.find_element(By.ID, "tuning")
    print(tuning.text)


# In[5]:


import tkinter as tk


# In[ ]:


from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("1000x100")
def show():
   print(val2)
   top.destroy()
   
val2 = askstring("Input", "Enter you name")   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()
from textblob import TextBlob
b = TextBlob(val2)
val2=b.correct()
runner()


# In[8]:


print(val2)


# In[6]:


pip install -U textblob

