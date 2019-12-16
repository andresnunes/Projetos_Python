'''
Exercise 3: Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
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
        di[word]=di.get(word,0) + 1

print(di)