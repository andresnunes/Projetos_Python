'''
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
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
        if len(words) < 3: continue
        word = words[2]
        di[word]=di.get(word,0) + 1

print(di)