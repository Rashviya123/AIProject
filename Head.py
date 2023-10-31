# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:54:03 2023

@author: Mohamed Mustafa
"""

import numpy as np
import pandas as pd
import sqlite3 as db
import subprocess

def is_valid_mobile_number(y):
    if len(y) == 10 and y.isdigit():
        return True
    else:
        return False

def is_valid_email(z):
    if '@' in z and '.' in z:
        return True
    else:
        return False
    
x=str(input('Enter your name'))
y=input('Enter your phone no')
while not is_valid_mobile_number(y):
    print("Invalid mobile number. Please enter a 10-digit number.")
    y = input("Enter a mobile number: ")
    
    
z=input('Enter your Mail id')
    
while not is_valid_email(z):
    print("Invalid email address. Please enter a valid email.")
    z = input("Enter an email address: ")
    
a = np.array([x])
b = np.array([y])
c = np.array([z])
frame={"Name":a,"Phone no":b,"Mail id":c}
df = pd.DataFrame(frame)
print(df)
database = "D:\Samplebot.sqlite"
conn = db.connect(database)
df.to_sql(name='Users', con=conn,if_exists='append',index=False)
conn.close()


result2 = subprocess.run(["python", "Timeloop.py"], capture_output=True, text=True)
print(result2.stdout)




