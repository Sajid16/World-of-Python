date1 = 7
date2 = 16

for x in range(31):
    if x == int(date1):
        print("this is your certificate birth date")
        continue
    elif x == int(date2):
        print("this is your real birth date")
        break