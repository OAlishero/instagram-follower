#!/usr/bin/env python3
#Alisher Yokubjonov
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random as r
import string
import time 

class Instagram: 
    def __init__(self):
        self.d = webdriver.Chrome(executable_path='/home/alisher/Desktop/IB/Drivers/chromedriver') #your driver directory
        self.d.get('https://www.instagram.com/')
        time.sleep(3)
        self.d.find_element_by_name('username').send_keys('username') #Insert your username/email/ or phone number as string
        self.d.find_element_by_name('password').send_keys('password') #Insert your password here as string
        self.xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        time.sleep(3) 
        self.xpath('//section/main/div/div/div/div/button').click() #save login info popup 
        self.waits(10,'/html/body/div[4]/div/div/div/div[3]/button[2]')
        self.xpath('//body/div[4]/div/div/div/div[3]/button[2]').click() #receive notifications window
    
    def waits(self,time,xpath): 
        try:
            element = WebDriverWait(self.d, time).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            
        except: 
            print("runtime error")
    
    def xpath(self, xpath): 
        button= self.d.find_element_by_xpath(xpath)
        return button

    def suggested(self): 
        self.a_file = open("privateaccounts.txt", "r")
        for line in self.a_file:
            line= line.strip() 
            self.privateuser="https://www.instagram.com/"+line+"/" #send user to the private acc
            self.d.get(self.privateuser) 
            time.sleep(3) 
            for i in range(0,5): #like 5 posts
                if i>2: 
                    self.postnum='2' #posts are split into two lines
                else: 
                    self.postnum='1'
                self.type=3

                try: 
                    self.xpath("//*[text()='No Posts Yet']")
                    print("checked if acc has pics")
                    self.type=5  #no posts
                except: 
                    pass

                try: 
                    self.xpath("//*[text()='This Account is Private']")
                    print("checked if acc is private")
                    self.type=6 #private
                except: 
                    pass

                if self.type==5: #if no posts
                    print('Not enough posts')
                    break

                try:
                    print('trying to like posts')
                    self.post= '//article/div[1]/div/div['+self.postnum+']/div['+str(i%3+1)+']/a'
                    self.waits(5,self.post)
                    self.xpath(self.post).click()
                    self.postlike= '//article/div[2]/section[1]/span[1]/button'
                    self.waits(15,self.postlike) #like the post
                    self.xpath(self.postlike).click()
                    self.xpath('/html/body/div[4]/div[3]/button').click() #exit out 
                    self.d.execute_script("window.history.go(-1)")
                except: 
                    break
            self.d.execute_script("window.history.go(-1)")
    def run(self): 
        self.running = True
        while self.running:
            self.suggested()

ig = Instagram()
while True:
    ig.run()
        