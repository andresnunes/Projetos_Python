'''
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average.

Enter file:mbox.txt
38444.0323119

Enter file:mbox-short.txt
39756.9259259
'''
import re

try:
    file=input("Enter a file: ")
    hfile = open(file)
except:
    print("Bad file")
    quit()

count = 0
total = 0
for line in hfile:
    line = line.rstrip()
    x = re.findall("^New Revision: ([0-9.]+)",line)
    if len(x)>0 : 
        num = float(x[0])
        total += num
        count += 1

print(total/count)