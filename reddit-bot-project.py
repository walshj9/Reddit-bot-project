import os
import praw
import sys

with open('../reddit-bot-data.txt') as f:
    info = f.read().splitlines()


uname = info[0]
pw = info[1]
acc_id = info[2]
acc_secret = info[3]
evlis_passw = info[4]
agent = 'school_project-bot by /u/school_project-bot'

#logs into reddit
def login():
    redditauth= praw.Reddit(client_id = acc_id,
                     client_secret = acc_secret,
                     password = pw,
                     user_agent= agent,
                     username= uname)
    return redditauth.user.me()

#gets suthorization link
def get_auth_link():
    auth_link = praw.Reddit(client_id= acc_id,
                        client_secret = acc_secret,
                        redirect_uri = 'http://localhost:8080',
                        user_agent = agent )
    return auth_link.auth.url(['identity'], '...', 'permanent')

reddit = praw.Reddit(user_agent=agent,
                     client_id=acc_id, client_secret=acc_secret,
                     username=uname, password=pw)

for submission in reddit.subreddit('all').hot(limit=30):
    print(submission.title)
    print(submission.score)
    print(submission.is_original_content)

print("\nPass")
