# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:44:35 2023

@author: Mohamed Mustafa
"""

import time
import pandas as pd
import sys
from fuzzywuzzy import fuzz



time_limit = 30
start_time=time.time()
end_time=start_time+time_limit
print("Hai, My name is Ria, a mobile shop bot, Welcome!")
print("How can I help you with today?")

def read(name):
    try:
        df = pd.read_excel(name+'.xlsx')  
        print(df.head(20))
    except:
        print('Sorry! some error occured')
        
def read1(name):
    try:
        df = pd.read_excel(name+'.xlsx')  
        print(df.iloc[21:30])
    except:
        print('Sorry! some error occured')
        
def more(name):
    q=input("Do you want more items: Y | N - ")
    if(q.lower()=='yes' or q=='y'):
        read1(name)
    else:
        msg()

def msg():
    print('Thanks for your chat! Hava a nice day')
    sys.exit()

def moreQueries():
    c = input('Do you have any more queries: Y | N - ')
    if c.lower() =='yes' or c.lower()=='y':
        run()
    else:
        msg()
    
#b =['models available','variety models','types of models','kinds of model']
def run():
    while time.time()<end_time:
       time.sleep(1)
       z = input("Let me know your query:")
       a = 'Samsung'
       b = ['brands','all mobiles']
       c = '5g'
       d = 'latest model'
       e = 'Google'
       f = 'Oppo'
       g = 'Real me'
       h = 'Oneplus'
       i = 'Vivo'
       j = 'Panasonic'
       k = ['Xioami','mi','Redmi']
       l = 'lava'
       m = 'Oled display'
       n = 'amoled display'
       o = 'lcd display'
       p = 'Nokia'
       q = 'Micromax'
       r = 'Coolpad'
       s = ['iphone','apple']
       if(fuzz.WRatio(a, z)>80): 
           read("Samsung")
           more("Samsung")
           moreQueries()
       elif(fuzz.WRatio(b[0],z)>80 or fuzz.WRatio(b[1],z)>80):
            read("brands1")
            moreQueries()
       elif(fuzz.WRatio(c,z)>80):
            read("5G smartphones")
            more("5G smartphones")
       elif(fuzz.WRatio(d,z)>80):
             read("latestModel")
             more("latestModel")
       elif(fuzz.WRatio(e,z)>80):
             read("Google")
             more("Google")
       elif(fuzz.WRatio(f,z)>80):
             read("Oppo")
             more("Oppo")
       elif(fuzz.WRatio(g,z)>80):
            read("Realme")
            more("Realme")
       elif(fuzz.WRatio(h,z)>80):
             read("Oneplus")
             more("Oneplus")
             moreQueries()
       elif(fuzz.WRatio(i,z)>80):
             read("Vivo2")
             more("Vivo2")
             moreQueries()
       elif(fuzz.WRatio(j,z)>80):
              read("Panasonic")
              more("Panasonic")
              moreQueries()
       elif(fuzz.WRatio(k[0],z)>80 or fuzz.WRatio(k[1],z)>80 or fuzz.WRatio(k[2],z)>80):
              read("Xiaomi")
              more("Xiaomi")
              moreQueries()
       elif(fuzz.WRatio(l,z)>80):
              read("Lava")
              more("Lava")
              moreQueries()
       elif(fuzz.WRatio(m,z)>80):
            read("Oled")
            more("Oled")
            moreQueries()
       elif(fuzz.WRatio(n,z)>80):
              read("Amoled")
              more("Amoled")
              moreQueries()
       elif(fuzz.WRatio(o,z)>80):
              read("Lcd")
              more("Lcd")
              moreQueries()
       elif(fuzz.WRatio(p,z)>80):
              read("Nokia")
              more("Nokia")
              moreQueries()
       elif(fuzz.WRatio(q,z)>80):
              read("Micromax")
              more("Micromax")
              moreQueries()
       elif(fuzz.WRatio(r,z)>80):
              read("Coolpad")
              more("Coolpad")
              moreQueries()
       elif(fuzz.WRatio(s[0],z)>80 or fuzz.WRatio(s[1], z)>80):
              read("iphone")
              more("iphone")
              moreQueries()
  
run()   
    
   
   

    

        
        
       
        #d = ['brands available','all mobiles','list all phones']
       
    
    
    