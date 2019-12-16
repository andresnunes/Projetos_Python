def computegrade(score):
    try:
        if score > 1.0 or score < 0.0:
            print("Value invalid")
            break
        elif score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "E"
    except: 
        print("Bad Score ")

s = float(input("Enter Score : "))
sc=computegrade(s)
print(sc)