'''
Send the words to Mirror Dimensions

Write a Python program that accepts a word from the user and reverse it.
Sample Test Case
Input : Edyoda
output: adoydE
'''
# program that accepts a word from the user and reverse it

def mirror_dimension(string):
    len_string = len(string)
    # reverse the order of string
    result = ""
    for char in string:
        result = char + result
    return result

string = input("Input a string to reverse: ")
result = mirror_dimension(string)
print("Reversed string is: ",result)
print("\n")

'''
tested & output as below 
single string - 
Input a string to reverse: Work
Reversed string is:  kroW

multiplt string -
Input a string to reverse: My Assignment is done
Reversed string is:  enod si tnemngissA yM

'''