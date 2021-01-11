# Do 'pip install praw' in your terminal before you run the program
import praw
import random, time, math

# Go to https://www.reddit.com/prefs/apps
# Click 'Create an App'
# Select 'script'
# Enter a name and description
# In redirect uri, put http://localhost:8080
# Create the app

# Your client_id is a 14 digit code at the top
# Your client_secret is the 25 digit code titled 'secret'
# Your user_agent is the name of your app
# Enter username and password of your reddit account

reddit = praw.Reddit(client_id="RMPRu8LDkNIChQ",
                     client_secret='OhbZUFk8u90r0IWLcXa98364vkGtVg',
                     user_agent='DM Script',
                     username='crimsontesting',
                     password='crimsontesting2020')

sub_list = "hwforcash+paidhomework+homework_marketplace+homeworkhelpwanted+paidhomeworkhelp"
subreddit = reddit.subreddit(sub_list)
old_post = ''
terms = ['physics', 'chemistry', 'biology', 'math', 'programming', 'economics']
queue = []
tag_list = ['for hire', 'hire me']

current_time = time.time()

# Add your header and message that you'd like to send to the users
HEADER = "Hi! I can help with your project!"


def check(string):
    for term in terms:
        if term in string.lower():
            return term
    return None


def pop():
    global queue
    queue = queue[1:]


def send_message(current_time, post):
    post_time = post[2]
    if post_time < current_time:
        author = post[0]
        term = post[1]
        MESSAGE = "Hey, I got you covered for " + term + " add me on Discord at Crimson#6271, I have vouches, and can solve an example question if needed."
        reddit.redditor(author).message(HEADER, MESSAGE)
        pop()


def reject_title(title):
    for tag in tag_list:
        if tag in title:
            return True
    return False


while True:
    current_time = math.floor(time.time())
    try:
        if queue:
            send_message(current_time, queue[0])
        posts = subreddit.new(limit=1)
        for new_post in posts:
            term = check(new_post.title)
            if not term:
                term = check(new_post.selftext)
            reject = reject_title(new_post.title.lower())
            if (new_post != old_post) and term and not reject:
                old_post = new_post
                queue.append((new_post.author.name, term, current_time + random.randint(300, 600)))
    except:
        pass
