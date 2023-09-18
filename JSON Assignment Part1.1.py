# Assignment 6 - JSON and OOP Assignment

# Part 1 Create an assignment for File handling of JSON files in Python
''' 1.1 
 Create a JSON file (employee.json) containing 
 Each employee information consists of Name, DOB, Height, City, State. 
 Write a python program that reads this  information from the JSON file and 
 saves the information into a list of objects of Employee class. 
 Finally print the list of the Employee objects.
'''

# import json module
import json 

# Creating 5 Employee Information to variable emp
emp = [
    { 'Name' : 'Raj', 'DOB' : '08th Jan 1995', 'Height' : 5.6, 'City' : 'Vizag', 'State' : 'Andhra Pradesh' },
    { 'Name' : 'Rani', 'DOB' : '08th Apr 1996', 'Height' : 5.4, 'City' : 'Vizag', 'State' : 'Andhra Pradesh' },
    { 'Name' : 'Nagraj', 'DOB' : '08th July 1997', 'Height' : 5.7, 'City' : 'Vizag', 'State' : 'Andhra Pradesh' },
    { 'Name' : 'Nagrani', 'DOB' : '08th Oct 1998', 'Height' : 5.5, 'City' : 'Vizag', 'State' : 'Andhra Pradesh' },
    { 'Name' : 'Maya', 'DOB' : '09th Nov 1990', 'Height' : 5.6, 'City' : 'Vizag', 'State' : 'Andhra Pradesh' }
]

# Creating Json File with above information
f1 = open('employee.json','w') # Directly from dictionary 
x = json.dumps(emp)
f1.write(x)
print(type(x))
f1.close()

# Reading Information of Json File
f1 = open('employee.json','r')
employee = json.loads(f1.read())
print(type(employee))
f1.close

#prints python object
print(employee)

