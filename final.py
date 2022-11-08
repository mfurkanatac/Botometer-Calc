import tweepy


name_list = []
save_to = open('name_list.txt', 'a') 

# API keys that yous saved earlier (have to be a twitter dev)
api_key = "x"
api_secrets = "x"
access_token = "x"
access_secret = "x"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit= True)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

# the screen_name of the targeted user (the one you want to get the followers of)
screen_name1 = "x"

counter = 0
# get the followers of the targeted user
# getting only 30 friends
for follower in tweepy.Cursor(api.followers, screen_name1).items(2476): # the items count is the number of followers of the targeted user
    print(follower.screen_name)
    save_to.write(follower.screen_name + '\n')
    counter += 1
    print(counter)

# reminder that there is a time limit for each API call. Check the twitter dev docs for more info.
