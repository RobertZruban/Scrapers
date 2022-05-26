#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
from selenium.common.exceptions import TimeoutException


import pprint
pp = pprint.PrettyPrinter(indent=4)
import random
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pyodbc
conn = pyodbc.connect(
"Driver={SQL Server};"
"Server=DESKTOP-F86F289\SQLEXPRESS;"
"Database =Heureka;"
"Trusted_Connection=yes;")





from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame()
list_heureka = ['https://notebooky.heureka.sk/','https://mobilne-telefony.heureka.sk', 'https://multifunkcne-zariadenia.heureka.sk/','https://monitory.heureka.sk/', 'https://prislusenstvo-k-hernym-konzolam.heureka.sk/',
                'https://mysi.heureka.sk/', 'https://inteligentne-hodinky.heureka.sk/','https://televizor.heureka.sk/','https://elektrobicykle.heureka.sk/'
                
                



]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
#chrome_options = browser.add_options('--no-sandbox') 


links = []
browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver', chrome_options=chrome_options)
  

for x in range(0,len(list_heureka)):
    for i in range (1,30) :
        try:
            url = list_heureka[x] + '/?f=' + str(i)
            browser.get(url)
            #time.sleep(1)
            html_source = browser.page_source  
            soup = BeautifulSoup(html_source,'html.parser')
            products = soup.findAll('a', class_='c-product__link')
            for product in products:
                links.append(product.get('href'))
           
           
           
            error = soup.findAll(class_ ='error-body')
            error = error[0].get_text()
            if error == 'Chyba Ospravedlňujeme sa, niečo sa nepodarilo.Zatiaľ môžete skúsiť prejsť na úvodnú stránku.Chyba 410':
                print("error")
                break
        except:
            pass

unique = list(set(links))
Top = []
Values_all = []
resellers = []
websites = []
item_names = []
prices = []
reviews = []
review_amounts = []
review_percentages = []
name_all = []
length = len(unique)
a = 0
z = 0


for item in unique[a:]:
    a = a + 1
    if a % 200 == 0:
        browser.quit()
        #time.sleep(1)
        browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver', chrome_options=chrome_options)
        browser.get(item)
    print(str(length - a) + "remaining")
    try:
        browser.get(item)
        result = None
        
    except requests.Timeout as err:
        ##cursor = conn.cursor()
        ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
        ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
        ##cursor.execute(SQL_command, Values)
        ##conn.commit()

        #browser.get(url)
        pass
    except requests.RequestException as err:
        ##cursor = conn.cursor()
        ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
        ##SQL_command = "INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);"
        ##cursor.execute(SQL_command, Values)
        ##conn.commit()

        #browser.get(url)
        pass


    except (ValueError,IndexError):
        ##cursor = conn.cursor()
        ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
        ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
        ##cursor.execute(SQL_command, Values)
        ##conn.commit()

        #browser.get(url)
        pass


   

    except Exception as e:
        pass


    while result is None:
        try:
            l = browser.find_element_by_xpath('//button[text(🙁"Zobraziť ďalšie ponuky"]')
            l.click()
            #time.sleep(1)
        
        
        except requests.Timeout as err:
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass
        except requests.RequestException as err:
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = "INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);"
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass
        

        except (ValueError,IndexError):
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass


        except TimeoutException as ex:
            browser.quit()
            browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver', chrome_options=chrome_options)
            pass
        
        
        except:
            result = "Not None"
            
            pass

    html_source = browser.page_source  
    soup = BeautifulSoup(html_source,'html.parser')
    kkt = soup.findAll('section', class_ = "c-offer")


    for i in range (0,50):
        try:
            reseller = kkt[i].find(class_ = "c-offer__shop-name u-color-text-light u-milli u-align-center").get_text()
            resellers.append(reseller)
            item_name = kkt[i].find(class_ = "c-offer__offer-shop-name").get_text()
            item_names.append(item_name)
            website = kkt[i].find(class_ = "c-offer__offer-name u-color-text-light u-milli").get('href')
            websites.append(website)
            price = kkt[i].findAll('span', class_ = "c-offer__price u-bold u-delta")
            price = price[0].get_text().replace(" €", "")
            prices.append(price)
            review = kkt[i].find(class_ = "c-offer-info-boxes__box").get_text()
            review_percentage = review[0:2]
            review_percentages.append(review_percentage)
            review_amount = review[review.find("%") + 1:].replace ("recenzií", "").replace(" ", "").replace("(","").replace(")","")
            review_amounts.append(review_amount)
            name =soup.findAll(class_ = 'c-product-info__name u-bold u-gamma')[0].get_text()
            name_all.append(name)




            # Getting the current date and time
            dt = datetime.now()

            # getting the timestamp
            ts = datetime.timestamp(dt)
            dt = str(dt)
            button = ''
            try:   
                button = soup.findAll(class_ = 'e-badge e-badge--top u-milli')[0].get_text()
            ##if not button:
                ##pass
            ##else:
                ##print('not empty')
            except Exception as e:
                pass
            Top.append(button)
            Values = [price,reseller,item_name,website,review_amount,button,dt,name]
            Values_all.append(Values)
            cursor = conn.cursor()
            SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price,reseler,item_name,website,review_amounts,topunit,time,name) VALUES (?,?,?,?,?,?,?,?);")
            cursor.execute(SQL_command, Values)
            conn.commit()



        except requests.Timeout as err:
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass
        except requests.RequestException as err:
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = "INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);"
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass
        

        except (ValueError,IndexError):
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()

            #browser.get(url)
            pass


        except TimeoutException as ex:
            browser.quit()
            browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver', chrome_options=chrome_options)
            pass
        
        except Exception as e:
            ##cursor = conn.cursor()
            ##Values = [prices[i],resellers[i],item_names[i],websites[i],review_amounts[i]]
            ##SQL_command = ("INSERT INTO Heureka.dbo.Heureka (price, reseler, item_name, website, review_amounts) VALUES (?,?,?,?,?);")
            ##cursor.execute(SQL_command, Values)
            ##conn.commit()
            #browser.get(url)
            pass

df['name'] = name_all
df["price"] = prices
df["reseler"] = resellers
df["item_name"] = item_names
df["website"] = websites
df["review_amounts"] = review_amounts
df["review_percentages"] = review_percentages

