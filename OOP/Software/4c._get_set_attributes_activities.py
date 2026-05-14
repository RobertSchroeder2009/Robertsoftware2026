class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def get_weight(self):
        return self.weight   

    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for the weight')
        else:
            print('please enter a number for the weight')

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)

p1.set_weight(12)

print('Bpnnies weight:',p1.weight)
p1.set_name(56789876)
print(p1.get_name())
print(p1)
#ACTIVITIES:
#1. Add attribute weight and write a getter method for weight
#2. Add setter method or weight and make sure it is a positive number (integer or float)