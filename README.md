# Botometer-Calc


https://rapidapi.com/OSoMe/api/botometer-pro/details

https://developer.twitter.com/en

  You firstly need to create a developer account and then rapidapi account. Rapidapi is needed for the botometer to calculate the probability for a given person to be a bot account. 
  In our work, we use tweepy (check tweepy docs) to pull follower list of a given person (if we want not just 1 user, we can increase the for loop counts for every user) and then we export it to a txt file. 
  Then using boto.py we calculate the probability and export it to another txt file which gives you the score out of 5. 
  
If there are any issues, be sure to ask about it. I will be as helpful as possible. 
