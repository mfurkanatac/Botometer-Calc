import botometer as bt

# we create an account for the botometer in rapidapi and get the key
rapidapi_key = "x"
twitter_app_auth = {
    'consumer_key': 'x',
    'consumer_secret': 'x',
    'access_token': 'x',
    'access_token_secret': 'x',
  } # twitter dev keys


# we authenticate the botometer
bom = bt.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

bobs_age = open('name_list.txt', 'r')
# Check a sequence of accounts
accounts = ["@" + acc[0:-1] for acc in bobs_age]
account_count = 0
bot_average = 0

for screen_name, result in bom.check_accounts_in(accounts):
    print(result)
    try: # sometimes botometer cannot come up with info for a user.
      if result["cap"]["universal"] > 2.5:
        print("Bot detected")
      account_count += 1
      bot_average += result["display_scores"]["universal"]["fake_follower"]

    except: # if botometer cannot come up with info for a user, we just skip it.
      pass

# we calculate the average bot score for the targeted user and print it.
# the higher the score, the more likely the user is a bot.
end_result = bot_average / account_count
print(end_result)
file = open("bot_result.txt", "w")
file.write(str(end_result))


