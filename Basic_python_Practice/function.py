def grading_system(marks):
    check = float(marks)
    if check >= 80:
        print('Congratulations! You have got A+')
    elif check >= 75:
        print('Congratulations! You have got A')
    elif check >= 70:
        print('Congratulations! You have got A-')
    elif check >= 65:
        print('Congratulations! You have got B+')
    else:
        print('You have to do better')


marks = input('Enter the average number to know the grade: ')
grading_system(marks)