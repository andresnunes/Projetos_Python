'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

'''

array = [[30, 75], [0, 50], [60, 150],[20,80],[85,170]]
count = 0
rooms = 1
for n in array: 
    if count == (len(array)-1):
        break
    inter1 = array[count]
    inter2 = array[count+1]
    if inter1[0] > inter2[0] and inter1[0] < inter2[1] and inter1[1] >= inter2[1]:
        print("Mais uma classe")
        rooms += 1 
    count += 1

print("Rooms required :",rooms)