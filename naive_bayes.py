# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:02:36 2018

@author: Kritika Mishra
"""

import newspaper
import nltk
from nltk.tokenize import word_tokenize
ny_paper = newspaper.build('https://www.aljazeera.com')
hotel_rev=["Hello"]
i=1
# Step 1 – Training data
train = [("Great place to be when you are in Bangalore.", "pos"),
  ("The place was being renovated when I visited so the seating was limited.", "neg"),
  ("Loved the ambience, loved the food", "pos"),
  ("The food is delicious but not over the top.", "neg"),
  ("Service - Little slow, probably because too many people.", "neg"),
  ("The place is not easy to locate", "neg"),
  ("Mushroom fried rice was spicy", "pos"),
]
  
# Step 2 
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
  
# Step 4 – the classifier is trained with sample data
classifier = nltk.NaiveBayesClassifier.train(t)

for article in ny_paper.articles:      
    url=article.url
    print(url)
    article.download()
    article.parse()
    a_txt=article.text
    hotel_rev.append(str(a_txt))
    i=i+1
    if(i==10):
        break
print(hotel_rev)
for test_data in hotel_rev:
    test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
    print (classifier.classify(test_data_features))
