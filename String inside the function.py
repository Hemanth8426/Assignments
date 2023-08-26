# String inside the function
'''
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''

def reverse_string(text):
     return text[::-1]

my_text = input('Enter a string: ')
reversed_string = reverse_string(my_text)
print(f'reverse of string {my_text} is: {reversed_string}')
