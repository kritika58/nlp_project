# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:19:08 2018

@author: Kritika Mishra
"""

import newspaper
#import pandas as pd
import csv
a=[]
cnn_paper = newspaper.build('https://www.bbc.com')
with open('output1.csv', 'w') as csvfile:
    fieldnames = ['art_url', 'art_text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    for article in cnn_paper.articles:
        url=article.url
        article.download()
        article.parse()
        a_txt=article.text
        writer.writerow({'art_url':url, 'art_text': a_txt})
        #print(a)
        #writer = csv.writer(writeFile)
        #writer.writerows(a)
        #print("Row added\n")