import math
print('Do you want to start the calculator?')
user_input = input("Yes or No (y/n) ")

if user_input == "yes" or user_input == "y":
    # print('here')
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    operator = input("enter the sign of the operator:(+,-,*,/,%) ")
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        result = num1 + num2
        final_result = float(result)
        print('the result of the addition is: ', final_result)
    elif operator == '-':
        result = num1 - num2
        final_result = float( result)
        print('the result of the subtraction is: ', final_result)
    elif operator == '*':
        result = num1 * num2
        final_result = float(result)
        print('the result of the multiplication is: ', final_result)
    elif operator == '/':
        if num2 == 0:
            num2 = input("Divisor cannot be 0.Enter the second number again: ")
            num2 = float(num2)
        result = num1 / num2
        final_result = float(result)
        print('the result of the division is: ', final_result)
    else:
        result = num1 % num2
        final_result = float(result)
        print('the result of the modulus is: ', final_result)

    print('''Do you want to get the result into integer or rounded value?
                 1.Integer
                 2.Round
                 3.Floor
                 4.Ceil
                 5.Exit\n''')
    user_input2 = input("Yes or No (1/2/3/4/5) ")
    if user_input2 == "1":
        final_result = int(final_result)
        print('the final result of the addition is: ', final_result)
    elif user_input2 == "2":
        final_result = round(final_result)
        print('the final result of the addition is: ', final_result)
    elif user_input2 == "3":
        final_result = math.floor(final_result)
        print('the final result of the addition is: ', final_result)
    elif user_input2 == "4":
        final_result = math.ceil(final_result)
        print('the final result of the addition is: ', final_result)
    else:
        print('Thanks for using this program.')
else:
    test = []
    test = input("enter the list of the numbers: ")
    print('''Do you want to get the result into integer or rounded value?
                     1.Maximum number
                     2.Minimum number\n''')
    user_input2 = input("Yes or No (1/2) ")
    if user_input2 == "1":
        print("The maximum number in the list is: ", max(test))
    else:
        print("The maximum number in the list is: ", min(test))

    print('Thanks for taking steps for your training.')