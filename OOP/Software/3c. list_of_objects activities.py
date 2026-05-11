# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = True

    def __str__(self):
        my_status = 'Names: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nCcredit: ' + self.ccard + '\nVaccination status: ' + str(self.vaccinated)
        if 'unknown' in self.ccard:
            print('no payment details registed')
        return my_status
    

p1 = Pet('John', 'Pork', age = 6)

p2 = Pet('sugar', 'bulldog')

pets = [p1, p2]

for pet in pets:
    print(pet)
    print('')
#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list