from datetime import date, timedelta
import praw

USERAGENT = "Wallpaper of the Week bot for /r/ComicWalls v1.0.0"
DATERANGE =[date.today().strftime('%B %d'), (date.today() - timedelta(7)).strftime('%B %d')]
SUBJECT = 'Top post from {0} to {1}!'.format(DATERANGE[1], DATERANGE[0])

def login():
    reddit = praw.Reddit("caps-bot", user_agent=USERAGENT)
    print("Logged in as: ", reddit.user.me())
    return reddit


def get_post(subreddit):
    top_post = subreddit.top('week').next()
    return top_post.shortlink

def send_modmail(subreddit, post):
    subreddit.message(SUBJECT, post)

reddit = login()
subreddit = reddit.subreddit('yakushatest')

post = get_post(subreddit)
send_modmail(subreddit, post)