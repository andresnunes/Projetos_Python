'''
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan
5 09:14:16 2008
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

diFlip = list()
for k,v in di.items():
    newtuple = (v,k)
    diFlip.append(newtuple)

diFlip.sort(reverse=True)

awnser = diFlip[0]

print("Awnser:",awnser[1],awnser[0])