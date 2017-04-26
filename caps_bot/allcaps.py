"""A bot which searches for reddit users who spell MF DOOM not in all caps. 

Keep bot information in a praw.ini either in the same directory as this script, or the correct config directory."""

import os
import re
import praw

USERAGENT = "CapsBot v1.2.0 by /u/Yakusha_"
REPLY_MESSAGE = "Just remember ALL CAPS when you spell the man name."


def login():
        r = praw.Reddit("caps-bot", user_agent=USERAGENT)
        return r



def find_word(string):
    regex = r'\b(mf doom|mf Doom|mf DOOM|Mf doom|Mf Doom|Mf DOOM|MF doom|MF Doom| Doom| doom)\b'
    return re.compile(regex).findall(string)


def task(reddit, replied):
    for comment in reddit.subreddit('yakushatest').comments(limit=20):
        if find_word(comment.body) and comment.id not in replied and comment.author != reddit.user.me():
            comment.reply(REPLY_MESSAGE)
            replied.append(comment.id)

            with open("replied.txt", "a+") as f:
                f.write(comment.id + "\n")

            with open("comments.txt", "a+") as f:
                f.write(comment.id + " - " + comment.body + "\n")


def replied_comments():
    if not os.path.isfile("replied.txt"):
        replied = []
    else:
        with open("replied.txt", "r") as f:
            replied = f.read()
            replied = replied.split("\n")
            replied = list(filter(None, replied))

    return replied


reddit = login()

replied_to = replied_comments()

task(reddit, replied_to)
