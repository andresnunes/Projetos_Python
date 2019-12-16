'''
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''

try:
    file=input("Enter a file: ")
    hfile = open(file)
except:
    print("Bad file")
    quit()


di = dict()
for line in hfile:
        words=line.split()
        for i in range(len(words)):
            word = words[i]
            for letter in word:
                if letter =='a' or letter == 'b' or letter == 'c' or letter == 'd' or letter == 'e' or letter == 'f' or letter == 'g' or letter == 'h' or letter == 'i' or letter == 'j' or letter == 'k' or letter == 'l' or letter == 'm' or letter == 'n' or letter == 'o' or letter == 'p' or letter == 'q' or letter == 'r' or letter == 's' or letter == 't' or letter == 'u' or letter == 'v' or letter == 'w' or letter == 'x' or letter == 'y' or letter == 'z':
                    di[letter]=di.get(letter,0) + 1

newlist = list()
for k,v in di.items():
    newtuple = (k,v)
    newlist.append(newtuple)

newlist.sort()

for k,v in newlist:
    print(k,v)
