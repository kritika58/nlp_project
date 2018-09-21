# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:58:09 2018

@author: Kritika Mishra
"""
import newspaper
file = open('positive.txt', 'r') 
p=file.read()
positive=p.split('\n')
#print(positive) 
file.close()
file = open('negative.txt', 'r') 
n=file.read()
negative=n.split('\n')
#print(negative) 
file.close()

f = open('output2.txt','a')

p_score=0
n_score=0
cnn_paper = newspaper.build('https://www.bbc.com')
for article in cnn_paper.articles:
    for i in range(5):        
            url=article.url
            print(url)
            article.download()
            article.parse()
            a_txt=article.text
            a_txt_arr=a_txt.split(' ')
            for word in a_txt_arr:
                if word in positive:
                    p_score=p_score+1
                elif word in negative:
                    n_score=n_score+1
            p_per=(p_score/(p_score+n_score))*100
            n_per=(n_score/(p_score+n_score))*100
            f.write('\n' + a_txt)
            f.write('\nPostive Score'+p_per)
            f.write('\nNegative Score'+n_per+'\n\n')
f.close()
        

