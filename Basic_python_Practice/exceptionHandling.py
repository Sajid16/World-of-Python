name = input('what is your name:\n')
print("Hello " + name + " \nWelcome to grading system\n")

while True:
    try:
        grade = int(input('Enter your number:\n'))
        if grade >= 80:
            print('Congratulation '+ name + ' You have got A+')
            break
        elif grade>= 75:
            print('Congratulation ' + name + ' You have got A')
            break
        elif grade>= 70:
            print('Congratulation ' + name + ' You have got A-')
            break
        elif grade >= 65:
            print('Congratulation ' + name + ' You have got B+')
            break
        else:
            print('Congratulation ' + name + ' You have got B')
            break

    except ValueError:
            print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    finally:
        print("See you soon.")