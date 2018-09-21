# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:52:14 2018

@author: Kritika Mishra
"""

#import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
  
hotel_rev = ["""MEXICO CITY — The morgue had a problem: It had run out of space for fresh corpses. Violence was soaring and new bodies were arriving every day, yet there was no place to store them.

Authorities in the western Mexican state of Jalisco hit on a short-term solution: They rented a refrigerated truck and parked it at the morgue, the Jalisco Institute of Forensic Sciences, near the state capital, Guadalajara. That was two years ago.

The stopgap measure seemed to be working fine — until the truck, with some 170 corpses on board, was driven off the lot on Sept. 7 and began a strange journey around the Guadalajara area, trailed by resident complaints of putrid smells and human rights denunciations of the inhumane treatment of the cadavers.

“Such events represent a lack of respect for the dignity of the deceased and violate their fundamental rights and those of their family members,” the National Human Rights Commission said Tuesday in a statement.""",
"Great place to be when you are in Bangalore.",
"The place was being renovated when I visited so the seating was limited.",
"Loved the ambience, loved the food",
"The food is delicious but not over the top.",
"Service - Little slow, probably because too many people.",
"The place is not easy to locate",
"Mushroom fried rice was tasty"]
  
sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()
