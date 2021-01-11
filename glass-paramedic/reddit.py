import praw
import random

reddit = praw.Reddit(client_id="LiRQ-jk4yiF_DA",
                     client_secret='tbbMaA7I7pNMdDwti7yAkNINwqyKWg',
                     user_agent='testing',
                     username='tester123456781609',
                     password='garbage2020')

limit = 500

def run(sub):
    subreddit = reddit.subreddit(sub)
    random_img = []
    post_list = subreddit.new(limit=limit)
    for submission in post_list:
        random_img.append(submission.url)
    return random.choice(random_img)