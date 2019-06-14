#!/usr/bin/python3

from googlesearch  import search
import time

x = input("enter what you want to search")

url=[]

for i in search(x,stop=10) : #take 10 links from google search page of our search
 print(i)
 time.sleep(2)

url.append(i)
print(url)