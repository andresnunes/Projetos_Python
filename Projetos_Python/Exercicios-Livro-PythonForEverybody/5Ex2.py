'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
'''
num = ""
count = 0
total = 0 
num_max = None
num_min = None
while num != "done":
    try:
        num = input("Enter a number :")
        if num == "done":
            break
        else:
            num = int(num)
        count = count + 1
        total = num + total
        if num_max is None:
            num_max = num
        if num_min is None:
            num_min = num
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num

    except:
        print("Invalid Input")
        continue
print("\nTotal: ",total,"\nNumber's Count: ",count,"\nMax: ",num_max,"\nMin: ",num_min)