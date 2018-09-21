import twitter
consumer_key='kEE3DM1v28wb5eNkxOR8oyA38'
consumer_secret='ZDuorWdbbl9HzTw0wnQpvXI3NyJcZbxsncRiCnjJL9RJsOepFn'
access_token_key='877193643341135872-IZ4ZQ29dZr3USnAyUgCCSwg88P0Ng3K'
access_token_secret='gIO13HApWBf24ey50MvTG7G5whUGIFoyLa3PP76PxmkdM'
api=twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token_key=access_token_key, access_token_secret=access_token_secret)
followers=api.GetFollowers()
#print(followers)
#search = api.GetSearch("happy") # Replace happy with your search
#for tweet in search:
    #print(tweet.id, tweet.text)
t = api.GetUserTimeline(screen_name="nytimes", count=100)
tweets = [i.AsDict() for i in t]
for t in tweets:
    print(t['id'], t['text'])
