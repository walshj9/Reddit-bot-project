import requests
import praw
import sys

with open('../reddit-bot-data.txt') as f:
    info = f.read().splitlines()
print(info)

uname = info[0]
pw = info[1]
acc_id = info[2]
acc_secret = info[3]
agent = 'school_project-bot by /u/school_project-bot'

redditauth= praw.Reddit(client_id = acc_id,
                     client_secret = acc_secret,
                     password = pw,
                     user_agent= agent,
                     username= uname)

reddit = praw.Reddit(client_id= acc_id,
                     client_secret = acc_secret,
                     redirect_uri = 'http://localhost:8080',
                     user_agent = agent )

print(redditauth.user.me())
print("\n")
print(reddit.auth.url(['identity'], '...', 'permanent'))
print("\nPass")
