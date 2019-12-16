'''
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

try:
    file=input("Enter a file: ")
    hfile = open(file)
except:
    print("Bad file")
    quit()

di = dict()
for line in hfile:
    if line.startswith("From "):    
        words=line.split()
        if len(words) < 2: continue
        word = words[1]
        address = word.split('@')
        domain = address[1]
        di[domain]=di.get(domain,0) + 1

print(di)