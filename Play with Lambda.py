#Q1. Play with Lambda
'''
Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
sample input: 10
sample output: 35
'''
add_25 = lambda num: num + 25

number = int(input('enter a number: '))
result = add_25(number)
print(f'result when added 25 to given number {number}: ', result) 
