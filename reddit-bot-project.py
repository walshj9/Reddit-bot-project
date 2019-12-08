import csv
import praw
from more_itertools import unique_everseen


with open('../reddit-bot-data.txt') as log_files:
    info = log_files.read().splitlines()


uname = info[0]
pw = info[1]
acc_id = info[2]
acc_secret = info[3]
agent = 'school_project-bot by /u/school_project-bot'

reddit = praw.Reddit(user_agent=agent,
                     client_id=acc_id, client_secret=acc_secret,
                     username=uname, password=pw)
print("logged in")
with open('reddit_data.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID','Title','Subreddit','Karma', 'No. of comments', 'OC', 'Upvote ratio', 'NSFW', 'Link'])
    lists = []
    for submission in reddit.subreddit('all').hot(limit=150):
        line = [str(submission.id),str(submission.title),str(submission.subreddit.display_name), int(submission.score),int(submission.num_comments), str(submission.is_original_content), float(submission.upvote_ratio), submission.over_18, submission.permalink]
        lists.append(line)
    rf = csv.writer(f, dialect='excel')
    rf.writerows(lists)
f.close()

print("Pass")

