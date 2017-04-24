Configuration
-------------
1. Install [praw](https://github.com/praw-dev/praw).
2. Store the account the bot should run in a `praw.ini` file as defined [here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

Running
-------
Either run this scrip as a cron job, or put `task(reddit, replied_to)` inside of a 'while True:`.
