def computepay(hours,rate):
    try:
        pay = hours * rate
        if hours > 40:
            pay = pay*1.5
        print("Pay : ",round(pay,2))
    except:
        print("Error, please enter a numeric input")

h = float(input("Enter Hours : "))
r = float(input("Enter Rate : "))

computepay(h,r)