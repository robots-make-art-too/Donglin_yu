import tweepy

consumer_key="3eeMdnGbDWebBN0p9i6L3HkrW"
consumer_secret="nES6nuNLiJa6THQe9YqeSrg8mj1kADTrq07In0tcdcco1f0GJh"
access_token="1494076192726691844-LPphEqMNW7vK4w3fqB9jtu5DAAiG1O"
access_secret="KojsVaBquAA7qA0xV3wPZRtUakk8snVKsW7LLtiFqvG3n"

auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
user = 'YorkUnews'
tweet_id = '1496141495765770252'
cc = 'to:{}'.format(user)
t = api.search_tweets(q=cc, since_id=tweet_id)
replies = 0
for i in range(len(t)):
    print(t[i].in_reply_to_status_id)
    if str(t[i].in_reply_to_status_id) == tweet_id:
        replies += 1
print(replies)
