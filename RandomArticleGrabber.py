import requests
import urllib.request

import wikipedia
import urllib.parse
import io
from sys import argv


def article(category):
    if (category=="All"):
        response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    else:
        response = requests.get("https://en.wikipedia.org/wiki/Special:RandomInCategory/" + category)
    if response.history:
        print (response.url)
    else:
        print ("Request was not redirected")
    url = urllib.parse.unquote(response.url)
    url = url.replace("https://en.wikipedia.org/wiki/","")
    url = url.replace("_"," ")
    wiki = wikipedia.page(url)
    print(wiki.title)
    print(wiki.content)
    #All available functions:
        #wiki.title - Get title of article
        #wiki.url - Get url of article
        #wiki.content - content title of article
        #wiki.links[0] - Get links of article
    target = io.open("Article.txt", 'w' , encoding='utf8')
    target.write(wiki.title)
    target.write("\n \n")
    target.write(wiki.content)
    target.close()
    return


