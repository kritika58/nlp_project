# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:02:36 2018

@author: Kritika Mishra
"""

import nltk
from nltk.tokenize import word_tokenize
  
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
  
test_data = """MEXICO CITY — The morgue had a problem: It had run out of space for fresh corpses. Violence was soaring and new bodies were arriving every day, yet there was no place to store them.

Authorities in the western Mexican state of Jalisco hit on a short-term solution: They rented a refrigerated truck and parked it at the morgue, the Jalisco Institute of Forensic Sciences, near the state capital, Guadalajara. That was two years ago.

The stopgap measure seemed to be working fine — until the truck, with some 170 corpses on board, was driven off the lot on Sept. 7 and began a strange journey around the Guadalajara area, trailed by resident complaints of putrid smells and human rights denunciations of the inhumane treatment of the cadavers.

“Such events represent a lack of respect for the dignity of the deceased and violate their fundamental rights and those of their family members,” the National Human Rights Commission said Tuesday in a statement."""
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
print (classifier.classify(test_data_features))