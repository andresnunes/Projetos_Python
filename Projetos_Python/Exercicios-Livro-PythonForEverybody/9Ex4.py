'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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

vmax = 0
kmax = None
for k,v in di.items():
    if vmax == 0:
        vmax = di[k]
    if di[k] > vmax:
        vmax = di[k]
        kmax = k

print("Max :", kmax,"=",vmax)