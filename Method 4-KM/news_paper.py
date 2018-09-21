from newspaper import Article

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

url='https://t.co/jKOiha8W9I'
article= Article(url)
article.download()
article.parse()
a_txt=article.text
#article.nlp()
#print(article.keywords)
p_score=0
n_score=0
a_txt_arr=a_txt.split(' ')
for word in a_txt_arr:
    if word in positive:
        p_score=p_score+1
    elif word in negative:
        n_score=n_score+1
p_per=(p_score/(p_score+n_score))*100
n_per=(n_score/(p_score+n_score))*100
print("Positive Score: ",p_per)
print("Negative Score: ",n_per)
