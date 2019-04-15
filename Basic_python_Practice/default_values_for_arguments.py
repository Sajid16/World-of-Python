def get_gender(sex):
    if sex == 'm':
        print("Male")
    elif sex == 'f':
        print("Female")
    else:
        print("unknown")

gender = input("Input your gender: m/f-> ")
get_gender(gender)