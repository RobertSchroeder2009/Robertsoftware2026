# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age, vaccination, ccredit, baddress, oname, funds):
        self.name = name
        self.category = category
        self.age = age
        self.vaccination = False
        self.ccredit = 'unknown'
        self.baddress = 'unknown'
        self.oname = 'unknown'
        self.funds = 0

p1 =  Pet('Bonnie', 'Cat', 3, True, '1847 3847 3904 8374', '37 south drive', 'John', 45.89)

p2 = Pet('Foxy',  'Dog', 5, True, '3874 9347 3975 7340', '84 Jakes way', 'James', '26.54')

print(p1.name)
print(p1.category)
print(p1.vaccination)

print(p2.name)
print(p2.category)
print(p2.vaccination)



#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)