# Fun with Lists and Tuples
'''
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
def last(n):
    return n[-1]

def sort(a):
    return sorted(a,key=last)

my_tup_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print('actual list: ',my_tup_list)
print('sorted: ', sort(my_tup_list))

'''
tested & output as 
actual list:  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted:  [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''