import csv
import praw
import pandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as yes
from fpdf import FPDF

with open('/home/walshj9/reddit-bot-data.txt') as log_files:
    info = log_files.read().splitlines()
uname = info[0]
pw = info[1]
acc_id = info[2]
acc_secret = info[3]
agent = 'school_project-bot by /u/school_project-bot'

reddit = praw.Reddit(user_agent=agent,
                     client_id=acc_id, client_secret=acc_secret,
                     username=uname, password=pw)

#with open('reddit_data.csv','w') as f:
#    writer = csv.writer(f)
#    writer.writerow(['ID','Title','Subreddit','Karma', 'Comment_count', 'OC', 'Upvote_ratio', 'NSFW', 'Link'])
#    lists = []
#    for submission in reddit.subreddit('all').hot(limit=150):
#        line = [str(submission.id),str(submission.title.replace(",","")),str(submission.subreddit.display_name), int(submission.score),int(submission.num_comments), str(submission.is_original_content), float(submission.upvote_ratio), submission.over_18, submission.permalink]
#        lists.append(line)
#    rf = csv.writer(f, dialect='excel')
#    rf.writerows(lists)
#f.close()


colnames = ['ID','Title','Subreddit','Karma', 'Comment_count', 'OC', 'Upvote_ratio', 'NSFW', 'Link']
data = pandas.read_csv('reddit_data.csv',names=colnames, skiprows=1)
subs = data.Subreddit.tolist()#?
sfw = data.NSFW.tolist()#pie
oc = data.OC.tolist()#pie
ratio= data.Upvote_ratio.tolist()#line
scores = data.Karma.tolist()#line

subCount = {i:subs.count(i) for i in subs}

tot=0
for i in scores:
    tot = tot + i
score_avg = tot/150

ymean = [score_avg]*150
ax = plt.subplots()
full_data = plt.plot(range(150),scores,label='Data', marker='o')
mean_line = plt.plot(range(150),ymean,label='Average -> '+str(score_avg),linestyle='--')
legend=plt.legend(loc='upper right')
plt.ylabel('Scores')
plt.xlabel('Live Position')
#plt.savefig('scores.png')
plt.clf()

trues = 0
for rating in sfw:
    if str(rating) == 'True':
        trues = trues +1
    else:
        pass
falses = 150-trues
labels = 'Not safe for work','Safe for work'
sizes=[trues,falses]
explode=(0.1,0)
colors = ['blue','red']
plt.pie(sizes, explode=explode, labels=labels, colors = colors,
        autopct='%1.1f%%', shadow=True, startangle = 140)
plt.axis('equal')
#plt.savefig('sfw.png')
plt.clf() 

orig = 0
for source in oc:
    if str(source) == 'True':
        orig = orig + 1
    else:
        pass
reposts = 150-orig
labels = 'Original Content', 'Repost'
sizes = [reposts,orig]
explode = (0, 0.1)
colors = ['blue','gray']
plt.pie(sizes,explode = explode, labels=labels, colors = colors,
        autopct='%1.1f%%', shadow=True, startangle = 90)
plt.axis('equal')
#plt.savefig('oc.png')
plt.clf()

rating = 0
for percent in ratio:
    rating = rating + percent
rating = rating/150
rate_mean = [rating]*150
bx = plt.subplots()
full_scores = plt.plot(range(150),ratio,label='Rating', marker='o')
avg_line = plt.plot(range(150),rate_mean,label = 'Average: '+str(rating), linestyle='--')
legend = plt.legend(loc= 'upper right')
plt.ylabel('Rating')
plt.xlabel('Index')
#plt.savefig('rating.png')
plt.clf()


