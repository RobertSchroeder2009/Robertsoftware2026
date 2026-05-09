#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:

names = ['rocky', 'ralph', 'hootie']
species = ['dog', 'human', 'blowfish']
age = ['8', '9', '34']
vac_stat = [True, False, True]

for i in range(len(names)):
  print(names[i])
  print(species[i])
  print(age[i])
  print(vac_stat[i])
  print('')
#ACTIVITIES:
# In each activity test out that the printing of data is still valid

#1. Add a new animal named Hootie, its a blowfish, it is 34 years
#done

#2. Vaccinate an unvaccinated animal (create vaccination)
#done

#3. Remove an animal and make sure that all the printing is correct
#Done