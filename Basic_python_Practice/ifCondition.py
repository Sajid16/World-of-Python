print("Enter the average number:\n")

# taking input here
a = input()

# converting input from string to integer
a = int(a)

a = a+2
# a = 80


if a >= 80:
    print('Congratulations!\nYou have got A+')
elif a>=75:
    print('Congratulations!\nYou have got A')
elif a >= 70:
    print('Congratulations!\nYou have got A-')
elif a >= 65:
    print('Congratulations!\nYou have got B+')
elif a >= 60:
    print('Congratulations!\nYou have got B-')
else:
    print('You have to do better\nBetter luck next time')

name = input("what is your name?\n" )

print("Welcome "+ name +" to the result maintain system")

if name != 'sajid':
    print("thank you unknown for being here")
    print(len(name))
# if name is "sajid":
#     print("thank you sajid for being here")
else:
    print("you are unknown to me")