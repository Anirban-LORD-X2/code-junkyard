import tweepy
import time

auth = tweepy.OAuthHandler('XXXXXXXXXXXXXXXXXXXXXXXXXXXx', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

api = tweepy.API(auth)

user=api.me()  
print(user.screen_name)
print(user.followers_count)

def limit_handler(cursor):  #Implementing a Limit handler
    while True:
        try:    
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)
#show the tweets in your timeline.            
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


#Bot will automatically follow back our followers

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Anish Dutta':
        
        follower.follow()

            
search_string='python'
numberOfTweets=2
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    
















