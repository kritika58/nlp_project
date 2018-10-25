# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:58:09 2018

@author: Kritika Mishra
"""
import newspaper
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

ny_paper = newspaper.build('https://www.economist.com')
sid = SentimentIntensityAnalyzer()
hotel_rev=["Hello"]   
for article in ny_paper.articles:      
    url=article.url
    print(url)
    article.download()
    article.parse()
    a_txt=article.text
    hotel_rev.append(str(a_txt))
for sentence in hotel_rev:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in ss:
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

        

