'''
8.14

Exercise 2: Figure out which line of the above program is still not
properly guarded. See if you can construct a text file which causes the
program to fail and then modify the program so that the line is properly
guarded and test it to make sure it handles your new text file.
'''

fhand = open('mbox-test.txt')
count = 0
for line in fhand:
    words = line.split()
    #gardian inside on the if statement
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])