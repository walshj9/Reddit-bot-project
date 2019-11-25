import os
import sys
import csv
import praw


with open('../reddit-bot-data.txt') as log_files:
    info = log_files.read().splitlines()


uname = info[0]
pw = info[1]
acc_id = info[2]
acc_secret = info[3]
agent = 'school_project-bot by /u/school_project-bot'

#logs into reddit
redditauth= praw.Reddit(client_id = acc_id,
                 client_secret = acc_secret,
                 password = pw,
                 user_agent= agent,
                 username= uname)
redditauth.user.me()

#gets suthorization link
auth_link = praw.Reddit(client_id= acc_id,
                    client_secret = acc_secret,
                    redirect_uri = 'http://localhost:8080',
                    user_agent = agent )
auth_link.auth.url(['identity'], '...', 'permanent')

reddit = praw.Reddit(user_agent=agent,
                     client_id=acc_id, client_secret=acc_secret,
                     username=uname, password=pw)

tot_score = 0

with open('dummycsv.csv', 'r+', newline= '') as f:
    fieldnames = ['ID', 'Subreddit', 'Karma']
    thewriter = csv.DictWriter(f, fieldnames)
    thewriter.writeheader()
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        iden = row['ID']
        sub = row['Subreddit']
        score = row['Karma']
        for submission in reddit.subreddit('all').hot(limit=5):
            if iden == submission.id:
                thewriter.write("{},{},{}".format(iden, sub, submission.score))

        #f.read()
        #print(submission.id)

        #for row in f:
        #    print(row)
        #    if submission.id in row[0]:
        #        row[2] = submission.score
            else:
                thewriter.writerow({'ID' : submission.id, 'Subreddit': submission.subreddit, 'Karma':submission.score})
        tot_score = tot_score + submission.score
f.close()

print("Average karma: ", tot_score/5)
print("\nPass")
