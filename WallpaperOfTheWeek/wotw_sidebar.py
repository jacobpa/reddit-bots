import praw

USERAGENT = "Wallpaper of the Week bot for /r/ComicWalls v1.0.0"


def login():
    reddit = praw.Reddit("yakusha_", user_agent=USERAGENT)
    print("Logged in as: ", reddit.user.me())
    return reddit


def get_post(subreddit):
    return subreddit.top('week').next()


def update_sidebar(subreddit, post):
    current_sidebar = subreddit.mod.settings()['description'].split('\n')
    current_sidebar[0] = '######[Wall of the Week by {0}]({1})'.format(post.author, post.shortlink)
    new_sidebar = '\n'.join(current_sidebar)
    subreddit.mod.update(description=new_sidebar)


reddit = login()
subreddit = reddit.subreddit('ComicWalls')

post = get_post(subreddit)
update_sidebar(subreddit, post)
