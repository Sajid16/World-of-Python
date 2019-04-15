class Parent:

    def print_last_name(self):
        print('Mahboob')


class Child(Parent):

    def print_first_name(self):
        print('Sajid')

    def print_last_name(self):
        print('Snitzleberg')


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()