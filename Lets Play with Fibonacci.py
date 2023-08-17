'''
Lets Play with Fibonacci

Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

'''
# Program to display the Fibonacci sequence up to n-th term

def Fibonacci(n,f,s):  # creating Fibonacci Function
    print(f,s,end=' ')
    for x in range(2,n):  
        next = f + s
        print(next,end=' ')
        f = s
        s = next        

nth_term = int(input("How many terms? "))  # asking nth term to user
first_term = 0  #assigning 1st term
second_term = 1 #assigning 2nd term
# check if the number of terms is valid
if nth_term <= 0:
   print("Please enter a positive integer")
# if there is only one term, return first_term
elif nth_term == 1:
   print("Fibonacci sequence upto",nth_term ,":",first_term)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   Fibonacci(nth_term,first_term,second_term)

'''
tested & output as below
How many terms? 50
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
1597 2584 4181 6765 10946 17711 28657 46368 75025 
121393 196418 317811 514229 832040 1346269 2178309 
3524578 5702887 9227465 14930352 24157817 39088169 
63245986 102334155 165580141 267914296 433494437 
701408733 1134903170 1836311903 2971215073 
4807526976 7778742049
'''