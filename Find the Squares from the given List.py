#Q3. Find the Squares from the given List
'''
Write a Python program to square the elements of a list using map() function.
Sample List:  [4, 5, 2, 9]
Square the elements of the list: [16, 25, 4, 81]
'''
number_list = list(map(int,input('enter list of numbers: ').split()))
print("Original List: ",number_list)
result = list(map(lambda x : x*x , number_list))
print(f'square the elements of the said list using map(): ', result)
