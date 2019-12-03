import os.path
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
exists = os.path.isfile('dummycsv.csv')
with open('dummycsv.csv', 'r+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID','Subreddit', 'Karma'])
    reader = csv.reader(f)
    data_list = list(reader)
    for submission in reddit.subreddit('all').hot(limit=5):
        line = [submission.id, submission.subreddit.display_name, str(submission.score)]    
        for row in data_list:#
            if str(row[0]) == str(submission.id) :#
                print("Removing: ", row)
                data_list.remove(row)
                data_list.append(line)
            else:#
                data_list.append(line)
                
    rf = csv.writer(f, dialect='excel')
    rf.writerows(data_list)
    #tot_score = tot_score + submission.score
f.close()

#print(data_list)
print("Average karma: ", tot_score/5)
print("\nPass")
