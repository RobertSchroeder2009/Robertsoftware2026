# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age = 0,):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0 


    def __str__(self):
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nccredit: ' + self.ccard + '\nVaccination status: ' + str(self.vaccinated)
        if 'unknown' in self.ccard:
            print('no payment details registed')
        return my_status
    

    def vaccinate(self):
        self.vaccinated = True

    def have_birthday(self):
        self.age += 1

    def clear_balance(self):
        self.account_balence = 0

    def calculate_human_age(self):
        if self.category == 'Dog':
            self.age*7
        if self.category == 'Cat':
            self.age*6

    
p1 = Pet('Bonnie', 'Cat', 10)    
p1.vaccinate()
print(p1)

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.