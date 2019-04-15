def dating_age(age):
    age = float(age)
    range_age = (age/2)+5
    return range_age

your_age = input("Enter your age: ")

dating_age = dating_age(your_age)
print("The range of age of your dating girlfriend has to be ",format(dating_age))