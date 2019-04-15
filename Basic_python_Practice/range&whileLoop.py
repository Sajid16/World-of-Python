print("first range values are:")
for x in range(10):
    print(x)

print("second range values are:")
for y in range(22,50,3):
    #print(y)
    y = int(y)
    if (y % 2) != 0:
        # print(y)
        # print('{0},it is an odd number'.format(y))
        print(y,'it is an odd number')
    else:
        # print("{0},it is an even number".format(y))
        print(y,'it is an even number')

number = 2
print("while loop function is starting from here")
while number < 10:
    print(number)
    number = number+1
