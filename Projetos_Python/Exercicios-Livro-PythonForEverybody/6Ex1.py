'''
Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
'''

string = input("Enter some text: ")
count = len(string)
while count > 0:
    print(string[count-1])
    count = count - 1

    