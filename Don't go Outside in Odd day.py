'''
Dont' go outside in Odd day

Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)   
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
'''
# program to count the number of even and odd numbers from a series of numbers.
series_number = tuple(input('Enter space-separated words: ').split())
print("Even and Odd Tuple Items : \n", series_number)
even_count = 0
odd_count = 0
for i in range(len(series_number)):
    if(int(series_number[i]) % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
print('Number of even numbers : ',even_count)
print('Number of odd numbers : ',odd_count)

'''
tested & output as below
Enter space-separated words: 1 2 3 4 5 6 7 8 9
Even and Odd Tuple Items :
 ('1', '2', '3', '4', '5', '6', '7', '8', '9')     
Number of even numbers :  4
Number of odd numbers :  5

'''