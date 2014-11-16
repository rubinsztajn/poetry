import sys
from textblob import TextBlob

def remove_non_ascii(s):
    return "".join(i for i in s if ord(i)<128)

poem_adj = open('poem_adj.txt', "w")
f = open(sys.argv[1], "r")
text = f.read().replace("\r", "")
text_clean = remove_non_ascii(text)

b = TextBlob(text_clean)

for tag in b.tags:
    if 'JJ' in tag:
        poem_adj.write(tag[0] + " ")



