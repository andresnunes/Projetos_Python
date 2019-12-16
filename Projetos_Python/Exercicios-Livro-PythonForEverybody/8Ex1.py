'''
Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
'''

def chop(li):
    li = li[1:-1]
    return None

def middle(li):
    li = li[1:-1]
    return li

l = [1,2,3,4,5]
m = middle(l)
print(m)

