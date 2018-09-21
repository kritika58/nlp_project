# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:46:38 2018

@author: Kritika Mishra
"""

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
'All my cats in a row',
'When my cat sits down, she looks like a Furby toy!',
'The cat from outer space',
'Sunshine loves to sit like this for some reason.'
]

vectorizer = CountVectorizer()
print( vectorizer.fit_transform(corpus).todense() )
print( vectorizer.vocabulary_ )