Configuration
-------------
1. Install [praw](https://github.com/praw-dev/praw).
2. Store the account the bot should run in a `praw.ini` file as defined [here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

Running
-------
* For both scripts, I recommend setting a cron job to run late every Saturday night, which will get the top post from the preceding Sunday to the current Saturday.
* For `wotw.py`, you can either use a unprivileged account, or a privileged mod account, but for `wotw_sidebar.py` the account the bot runs as **must** be a moderator for the subreddit.