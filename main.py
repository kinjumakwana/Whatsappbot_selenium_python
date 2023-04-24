from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.db import IntegrityError
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import re 
import pandas as pd
import csv
import os
CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\BAPS\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(CHROME_PROFILE_PATH)
options.add_argument('--profile-directory=Default')

# C:\Users\BAPS\AppData\Local\Google\Chrome\User Data
s = Service(r"D:\Kinjal\chromedriver_win32\chromedriver.exe")

class Whatsappbot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        WebDriverWait(self.driver, 5)
        print("Logged in successfully")
        
    def whatsappdata(self):
        try:
            sleep(10)
            # input("Press enter after scanning QR code")
            targets = ['"Ritesh Patel"','"Dineshbhai@aahaa"']
            message="Hello testing"
                   
            for target in targets:
                try:
                    contact_path='//span[contains(@title,'+ target +')]'
                    # contact_path='//span[contains(@title, {})]'.format(str(target))
                    
                    contact=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,contact_path)))
                    contact.click()
                    # sleep(5)
                    message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                    message_box=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,message_box_path)))
                    
                    message_box.send_keys(message + Keys.ENTER)
                    sleep(5)
                
                except Exception as e:
                    # print(f"Could not send message to {target}.")  
                    #   print(e)  
                    search_bar_path = '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]'
                    search_bar = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, search_bar_path)))
                    search_bar.click()
                    target1 = target.strip()
                    # print(target1)
                    target2 = target1.strip().replace('"', '')
                    # print(target2)
                    search_bar.send_keys(target2 + Keys.ENTER)
                    sleep(2)
                    message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                    message_box=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,message_box_path)))
                    message_box.send_keys(message + Keys.ENTER)
                    sleep(5)
                    # WebDriverWait(self.driver, 10)
                
                                
        except Exception as e:
            print(e)
            sleep(10)

Whatsapp = Whatsappbot()
Whatsapp.whatsappdata()
