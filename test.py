# A simple function extracting the tweets from trumptweet.json and export it as a list of splashes.
# Only count tweets with 5 words or less, no retweets, all images are stripped, no continuation from
# previous tweets.

# trumptweet.json contains every trump tweet from 2017-01-01 to 2020-07-09.

import json

f = open("trumptweet.json", "r", encoding="utf8")
tweetsRaw = f.read()
f.close()
parsed = json.loads(tweetsRaw)

listofvalidtweets = []

def fn(text):
    if text[0] == ".": return False
    if text[0:5] == "https": return False
    if text.count(' ') > 5: return False
    if text[0:2] == "RT": return False
    return True

for i in parsed:
    checkText = i["text"].replace("&amp;", "&").replace(" \n","").strip()
    index = checkText.find("https://t.co")
    if index >= 0:
        checkText = checkText[:index]
    if (not checkText in listofvalidtweets) and len(checkText) > 0 and fn(checkText):
        listofvalidtweets.append(checkText)
print(listofvalidtweets)
f = open("splashes.txt", "w", encoding="utf8")
tweetsRaw = f.write("\n".join(listofvalidtweets))
f.close()