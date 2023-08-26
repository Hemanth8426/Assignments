# Calculate the Upper and The lower Case of string
'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def upper_lower_string(text):
    upper = 0
    lower = 0
    for str in text:
        if str.isupper():
            upper += 1
        elif str.islower():
            lower += 1
        else:
            pass
    print(f'No. of Upper case characters in String \'{text}\' is: {upper}')
    print(f'No. of Lower case characters in String \'{text}\' is: {lower}')

my_text = input('Enter a string: ')
upper_lower_string(my_text)
