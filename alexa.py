#!/usr/local/bin/python3.7
import praw
import pdb
import re
import os
import random
import time

# Create the Reddit instance
reddit = praw.Reddit('alexaBot')
# Common part of the message
common = "\n\n───────────⚪──────────────────────────────── \n\n◄◄⠀▐▐ ⠀►►⠀⠀ ⠀ 1:17 / 4:20 ⠀ ───○ 🔊⠀ ᴴᴰ ⚙ \n\n ^I ^am ^a ^bot ^please ^direct ^any ^questions ^or ^concerns ^to ^/u/FestiveOx_"
despacito = ["ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito (ft. Justin Bieber)",
             "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito 3 (ft. Elon Musk & The Submarines)", "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito 4 (ft. NASA & Cardi B)", ]

if not os.path.isfile("comment_replied_to.txt"):
    comment_replied_to = []
else:
    with open("comment_replied_to.txt", "r") as f:
        comment_replied_to = f.read()
        comment_replied_to = comment_replied_to.split("\n")
        comment_replied_to = list(filter(None, comment_replied_to))

subreddit = reddit.subreddit("all")

for comment in subreddit.stream.comments():
    if comment.id not in comment_replied_to:
        if re.search("alexa play despacito 2", comment.body, re.IGNORECASE):
            comment.reply("ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito 2 (ft. Lil' Pump)" + common)
            comment_replied_to.append(comment.id)
            with open("comment_replied_to.txt", "w") as f:
                for comment_id in comment_replied_to:
                    f.write(comment_id + "\n")
        if re.search("alexa play despacito", comment.body, re.IGNORECASE):
            comment.reply(random.choice(despacito) + common)
            comment_replied_to.append(comment.id)
            with open("comment_replied_to.txt", "w") as f:
                for comment_id in comment_replied_to:
                    f.write(comment_id + "\n")
        if re.search("alexa play africa", comment.body, re.IGNORECASE):
            comment.reply("ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Africa by Toto" + common)
            comment_replied_to.append(comment.id)
            with open("comment_replied_to.txt", "w") as f:
                for comment_id in comment_replied_to:
                    f.write(comment_id + "\n")
