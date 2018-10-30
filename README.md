###### NLP- Sentiment Analysis

### Tools and Methodology
# Python
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.
# Anaconda
Anaconda is a free and open source distribution of the Python and R programming languages for data science and machine learning related applications that aims to simplify package management and deployment. Package versions are managed by the package management system conda.
# Twitter API
This library provides a pure Python interface for the Twitter API. It works with Python versions from 2.7+ and Python 3. Twitter provides a service that allows people to connect via the web, IM, and SMS. Twitter exposes a web services API and this library is intended to make it even easier for Python programmers to use.
pip install twitter-python
# Rosette
Rosette brings the power of AI to text analysis components within search, business intelligence, e-discovery, social media, financial compliance, and enterprises. Rosette returns sentiment scores for entire documents, or for individual entities within a larger body of text.
pip install rosette-api
# NLTK
NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
pip install nltk
import nltk
nltk.download()
# Newspaper3k
Newspaper is a Python module used for extracting and parsing newspaper articles. Newspaper use advance algorithms with web scrapping to extract all the useful text from a website. It works amazingly well on online newspapers websites.
pip install newspaper
# GDELT Project
The GDELT Project is an initiative to construct a catalog of human societal-scale behavior and beliefs across all countries of the world, connecting every person, organization, location, count, theme, news source, and event across the planet into a single massive network that captures what's happening around the world, what its context is and who's involved, and how the world is feeling about it, every single day.
 
### Naïve Bayes Classification 
In machine learning, naive Bayes classifiers are a family of simple "probabilistic classifiers" based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
Naive Bayes has been studied extensively since the 1950s. It was introduced under a different name into the text retrieval community in the early 1960s: 488 and remains a popular (baseline) method for text categorization, the problem of judging documents as belonging to one category or the other (such as spam or legitimate, sports or politics, etc.) with word frequencies as the features. With appropriate pre-processing, it is competitive in this domain with more advanced methods including support vector machines. It also finds application in automatic medical diagnosis.
Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. Maximum-likelihood training can be done by evaluating a closed-form expression, which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.
In the statistics and computer science literature, naive Bayes models are known under a variety of names, including simple Bayes and independence Bayes. All these names reference the use of Bayes' theorem in the classifier's decision rule, but naive Bayes is not (necessarily) a Bayesian method.

### NTLK Vader
For the English language, NLTK provides an already trained model called VADER (Valence Aware Dictionary and sEntiment Reasoner) that works in a slightly different way and adopts a rule engine together with a lexicon to infer the sentiment intensity of a piece of text.
The NLTK version uses the SentimentIntensityAnalyzer class and can immediately be used to have a polarity sentiment measure made up of four components:
•	Positive factor
•	Negative factor
•	Neutral factor

### Rosette Sentiment Analysis
Sentiment refers to the attitudes, opinions, and emotions of a person towards a person, place, thing, or other entity. These are subjective impressions, not facts. Rosette returns sentiment scores for entire documents, or for individual entities within a larger body of text.
A document refers to a body of text that expresses sentiment such as a review of a film, a political editorial, a Facebook status or a short tweet. An “awesome new movie” is positive, but a “disastrous political scandal” has a negative sentiment. 
What if the film review covers several movies? Which movies were more positively received than others? Here, Rosette applies entity extraction to identify the movies and determines the sentiment for each one by relating the sentiment in the review to each entity. Our sentiment analysis provides entity-level analysis for 18 entity types out of the box, but can be retrained to extract and analyse custom entity type’s on-premise.
