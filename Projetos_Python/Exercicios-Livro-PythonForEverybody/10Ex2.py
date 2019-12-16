'''
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.

Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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
        if len(words) < 6: continue
        word = words[5]
        time = word.split(':')
        hour = time[0]
        di[hour]=di.get(hour,0) + 1

newlist = list()
for k,v in di.items():
    newtuple = (k,v)
    newlist.append(newtuple)

newlist.sort()

for k,v in newlist:
    print(k,v)
    
