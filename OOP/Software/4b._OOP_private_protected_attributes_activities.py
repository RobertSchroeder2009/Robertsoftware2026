# Learning intentions:
# - Create a protected attribute
# - Create a private attribute

class Pet:
    def __init__(self, name, category, breed = None, age = 0,):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0 

    def set_name(self,new_name):
        self._name = new_name
        if type(new_name) == str:
            self._name = new_name
        else: print('Please use a string as a name attribute')
        
    def get_name(self):
        return self._name


    def __str__(self):
        my_status = 'Name: ' + self._name + '\nCategory: ' + self.__category + '\nAge: ' + str(self.age) + '\nccredit: ' + self.ccard + '\nVaccination status: ' + str(self.vaccinated)
        if 'unknown' in self.ccard:
            print('no payment details registed')
        return my_status

    
p1 = Pet('Bonnie', 'Cat', 10)    
p1.set_name('Bonniffer')
print(p1)

   

#ACTIVITIES:
#1. Make category a private attribute than test to make sure it can't be changed once created
#2. Add another private attribute for breed 