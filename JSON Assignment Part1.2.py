# Assignment 6 - JSON and OOP Assignment

# Part 1 Create an assignment for File handling of JSON files in Python

''' 1.2 
Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
'''

import json

states = {} # created empty dictionary
num = int(input('Enter number of states are there: ')) 
for i in range(num):
    state = input('Enter name of state: ')
    capital = input('Enter name of capital: ')
    states[state] = capital # inserting data into dictionary
   
# printing dictionary info
print('Created dictionary is: ')
print(states)

# Creating Json File with above information
f1 = open('states_capital.json','w') # Directly from dictionary 
x = json.dumps(states)
f1.write(x)
f1.close()

print('Jason File Created based on above dictionary')

