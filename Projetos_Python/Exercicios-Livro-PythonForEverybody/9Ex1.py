'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
'''

value = 0
di = dict()
hfile = open("words.txt")
for line in hfile:
    words = line.split()
    for word in words:
        di[word] = value
        value += 1

check = input("Enter a word to check: ")
if check in di:
    print("True!!")
else:
    print("False!!")
