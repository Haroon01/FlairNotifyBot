import praw
import time

# FlairyBot
# ACoolBot54!
# the above are details for the account "FlairyBot" which is used to PM you on reddit.


reddit = praw.Reddit(client_id='FTwCG3MILzD61w',
                     client_secret='qEjosVQHQIFtEhCZZUywGVxDdBs',
                     username="FlairyBot",
                     password="ACoolBot54!",
                     user_agent='Flair bot by u/ItsTheRedditPolice')


# BUG: sends pm with the last 8 posts from r/creatorservices

def scansub(sub):
    # --------- Add your flairs you would like to track here! ---------------
    flairs = ["Looking For Paid Services", "Hiring", "Hiring - Open", "Task"]
    # -------------------------------------------------------------------------
    for submission in reddit.subreddit(sub).stream.submissions():
        rawtitle = submission.title
        title = rawtitle.split()
        flair = submission.link_flair_text
        link = submission.permalink
        subreddit = submission.subreddit
        if flair in flairs:
            reddit.redditor('ItsTheRedditPolice').message(f'Match found in r/{subreddit}!',
                                                          f'I have found a post containing your flair(s): {flair}\n\n'
                                                          f'Title: {rawtitle}\n\nLink: {link}')
            print(f"* Match Found! Sent a PM! ({flair} - {rawtitle})")
        else:
            pass


print(f"Successfully logged in as: {reddit.user.me()}\n----------------------------------------------------")
time.sleep(5)
print("Bot is now running!\nKeep this window open to keep the bot running!\n"
      "------------Bot by u/ItsTheRedditPolice-------------")
time.sleep(1)


while True:
    # ------- Write down the subreddits you want to track using the bot ---------------
    # E.g. i want to track r/askreddit and r/pics:
    #    scansub("askreddit")
    #    scansub("pics")

    scansub("creatorservices")
    scansub("forhire")
    scansub("slavelabour")
