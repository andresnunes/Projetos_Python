'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''

import urllib.request, urllib.parse, urllib.error

url = input("Enter a site: ")
if url=="":
    url = "http://data.pr4e.org/romeo.txt"
try:
    urlSplit = url.split('/')
    host =  urlSplit[2]
except:
    print("Bad url")
    quit()

fhand = urllib.request.urlopen(url)
di = dict()
count = 0
for line in fhand:
    words = line.decode().strip()
    for word in words:
        if count >= 3000:
            break
        count += 1
        di[word]=di.get(word,0) + 1

newlist = list()
for k,v in di.items():
    newtuple = (v,k)
    newlist.append(newtuple)

newlist.sort(reverse=True)

for v,k in newlist:
    print(v,k)