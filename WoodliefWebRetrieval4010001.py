import urllib.request
import re

def run():
    count = 0
    myList = []

    for item in re.findall(r'(<a[\s]+href="http([^>]+)>((?:.(?!\<\/a\>))*.)<\/a>)', getWiki().read().decode("utf-8")):
         count += 1
         myList.append(item)

    myFile = open("output.txt", "w+")
    myFile.write(f"number of urls: {count}\n")
    for item in myList:
        myFile.write(f"{item}\n")

def getWiki():
    return urllib.request.urlopen('https://en.wikipedia.org/wiki/The_Beatles')

run()
