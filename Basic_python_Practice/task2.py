def food_choice(serial):
    choice = int(serial)
    item = 0
    if choice == 1:
        list = []
        list = input('Please enter which ingredients do you want?' )
       # print(list)
        for l in list:
            if l == "," or l == ".":
                item = item+1
        print("you have selected {0} items. they are:".format(item))
        print(list)
        time = item*5;
        print("It will take {0} minutes to serve your food.\nPlease wait and thanks fro coming here.".format(time))
    elif choice == 2:
        list = []
        list = input('Please enter which ingredients do you want?' )
       # print(list)
        for l in list:
            if l == "," or l == ".":
                item = item+1
        print("you have selected {0} items. they are:".format(item))
        print(list)
        time = item*5;
        print("It will take {0} minutes to serve your food.\nPlease wait and thanks fro coming here.".format(time))
    else:
        list = []
        list = input('Please enter which ingredients do you want?' )
       # print(list)
        for l in list:
            if l == "," or l == ".":
                item = item+1
        print("you have selected {0} items. they are:".format(item))
        print(list)
        time = item*5;
        print("It will take {0} minutes to serve your food.\nPlease wait and thanks for coming here.".format(time))

print("Which of the following foods do you want?")
print("1.burger\n2.Pizza\n3.Pasta")
choice = input("Enter your choice: ")
food_choice(choice)