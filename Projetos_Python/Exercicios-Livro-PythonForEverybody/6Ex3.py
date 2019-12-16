'''
Exercise 3: Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments.
'''

def count(string,letter):
    count = 0
    for x in string:
        if x == letter:
            count += 1
    return count 

word = "banana"
letter = "b"
print(count(word,letter))