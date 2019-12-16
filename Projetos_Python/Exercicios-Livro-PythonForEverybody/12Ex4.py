'''
Exercise 4: Change the urllinks.py program to extract and count para-
graph (p) tags from the retrieved HTML document and display the
count of the paragraphs as the output of your program. Do not display
the paragraph text, only count them. Test your program on several
small web pages as well as some larger web pages.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#taking the url from the user
url = input('Enter a url: ')
if url == "":
    url = 'https://docs.python.org'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

htmlTag = input("Enter a Tag: ")

#Counting all p tags
count = 0
tags = soup(htmlTag)
for tag in tags:
    count += 1

print ("Total:",count)