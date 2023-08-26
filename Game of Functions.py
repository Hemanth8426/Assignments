# Game of "Functions"
'''
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
Explanation: Summation should like 8+2+3+0+7 = 20
'''

def sum_of_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

list_numbers = list(map(int,input('Enter values of List seaparated by space: ').split()))
sum_numbers = sum_of_list(list_numbers)
print(f'sum of numbers in list {list_numbers} is: {sum_numbers}')
