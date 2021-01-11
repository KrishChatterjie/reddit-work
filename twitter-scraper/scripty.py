import snscrape.modules.twitter as sntwitter
import csv
import emoji
import re

# Creating list to append tweet data to
tweets_list2 = []

keywords = ["scanxiety", "scananxiety", "scan anxiety", "scan-anxiety", "scan-related anxiety", "scan-associated anxiety"]
months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "April", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec",}

with open('scanxiety2018.csv', mode='w') as csv_file:
    
    fieldnames = ['date', 'handle', 'url', 'x','comments', 'retweets', 'likes', 'emoji', 'content', 'type', 'userbio', 'location', 'keyword', 'hashtag', 'media', 'link', ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('("scanxiety" OR "scananxiety" OR "scan anxiety" OR "scan-anxiety" OR "scan-related anxiety" OR "scan-associated anxiety") since:2018-01-01 until:2018-12-31').get_items()):
        
        year = str(tweet.date)[:4]
        month = months[int(str(tweet.date)[5:7])]
        day = str(tweet.date)[8:10]
        
        date = day + '-' + month
        handle = tweet.user.username
        url = tweet.url
        comments = tweet.replyCount
        if comments == None:
            comments = 0
        retweets = tweet.retweetCount
        if retweets == None:
            retweets = 0
        likes = tweet.likeCount
        if likes == None:
            likes = 0

        content = tweet.content
        emojis = ' '.join(c for c in content if c in emoji.UNICODE_EMOJI)

        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        content = regrex_pattern.sub(r'', content)      

        if content[0] == '@':
            orq = 'R'
        elif tweet.quotedTweet != None:
            orq = 'Q'
        else:
            orq = 'O'
        
        userbio = tweet.user.description
        location = tweet.user.location

        key = ''
        for keyword in keywords:
            if keyword in content.lower():
                key = key + keyword + ','
        if key:
            key = key[:-1]
        
        hashtags = ''
        links = ''
        x = content.split()
        for word in x:
            if 'http' in word:
                links = links + word
            elif word[0] == '#':
                hashtags = hashtags + word[1:] + ','
        if links:
            links = links[:-1]
        if hashtags:
            hashtags = hashtags[:-1]
        media = tweet.media
        
        content = content.encode('unicode_escape')
        emojis = emojis.encode('unicode_escape')
        userbio = userbio.encode('unicode_escape')

        try:
            writer.writerow({'date': date,
                            'handle': handle,
                            'url': url,
                            'comments': comments,
                            'retweets': retweets,
                            'likes': likes,
                            'emoji': emojis,
                            'content': content,
                            'type': orq,
                            'userbio': userbio,
                            'location': location,
                            'keyword': key,
                            'hashtag': hashtags,
                            'media': media,
                            'link':links
                            })
        except:
            print(url)




# print(tweets_list2)