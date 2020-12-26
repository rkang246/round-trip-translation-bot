import praw
from translate import Translator
import random

# CONFIG
num_iterations = 3

# Initialize Translator Codes
iso_codes = ["zh", "ru", "ja", "ar", "ko", "pt", "en", "it", "el", "fr", "en"]

translators = []
for lang in iso_codes:
    translators.append(Translator(to_lang=lang))

toEn = Translator(to_lang="en")

# Password Authentication Flow via praw.ini
reddit = praw.Reddit("RTT")
for comment in reddit.subreddit("askreddit").comments(limit = 1):
    print("----------")
    comment_body = comment.body
    print(comment_body)

    for i in range(0, len(translators)):
        comment_body = translators[i].translate(comment_body)
        print("translating to ", iso_codes[i], "(", comment_body ,")")

    '''
    for i in range(0, num_iterations):
        rand = random.randint(0, len(translators))
        print(rand)

        comment_body = translators[rand].translate(comment_body)
        print("translating to ", iso_codes[rand], "(", comment_body ,")")

    comment_body = toEn.translate(comment_body)
    print("Final English Return:", comment_body)
    '''
