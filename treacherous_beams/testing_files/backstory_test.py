import random, time 
Sty = ""
yynn = ["Yes", "yes", "No", "no"]

#-----------------------------------------

print("Do you know your backstory[Yes/No]")
Sty = input("")
print('')

while Sty not in yynn:
  print("Please type it with a capital letter")
  Sty = input('')

if 'Yes' in Sty:
    Story = input('[Please type you backstory here]')
    print('Oh wow such a interesting story...')
    print(f'Really? {Story}?')

elif 'yes' in Sty:
    Story = input('[Please type you backstory here]')
    print('Oh wow such a interesting story...')
    print(f'Really? {Story}?')


elif 'No' in Sty:
    print('A story will be randomly selected for you')

elif 'no' in Sty:
    print('A story will be randomly selected for you')
