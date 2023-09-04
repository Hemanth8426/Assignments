#Q2. Find the way with Maps
'''
Write a Python program to triple all numbers of a given list of integers. Use Python map.
sample list:  [1, 2, 3, 4, 5, 6, 7]
Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]
'''
number_list = list(map(int,input('enter list of numbers: ').split()))
print("Original List: ",number_list)
result = list(map(lambda x : x*3 , number_list))
print(f'triple to all numbers of the said list using map(): ', result)
