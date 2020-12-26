import praw

# Password Authentication Flow via praw.ini
reddit = praw.Reddit("RTT")
print(reddit.user.me())