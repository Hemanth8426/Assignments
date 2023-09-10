# Challenge 2: Implement a Calculator Class
# implement a calculator that can perform addition, 
# subtraction, multiplication, and division.

class Calculator:
    def __init__(self,number1,number2):
        self.x = number1
        self.y = number2
    def add(self):
        return self.x + self.y
    def subtract(self):
        if self.x < self.y:
            return self.y - self.x
        elif self.x - self.y:
            return self.x - self.y
        else:
            return 0
    def multiply(self):
        return self.x * self.y
    def divide(self):
        if self.y != 0:
            if self.x < self.y:
                return self.y / self.x
            elif self.x > self.y:
                return self.x / self.y
            else:
                return 1
        else:
            return('can not be divide by 0')

def main():
    number1 = input('enter a first number: ')
    number2 = input('enter a second number: ')
    if '.' in number1:
        number1 = float(number1)
    else:
        number1 = int(number1)
    if '.' in number2:
        number2 = float(number2)
    else:
        number2 = int(number2)
    obj_calc = Calculator(number1,number2)
    add_numbers = obj_calc.add()
    print(f'addition of {number1} & {number2} is ',add_numbers)
    sub_numbers = obj_calc.subtract()
    print(f'subtraction of {number1} & {number2} is ',sub_numbers)
    mul_numbers = obj_calc.multiply()
    print(f'multiplication of {number1} & {number2} is ',mul_numbers)
    div_numbers = obj_calc.divide()
    print(f'division of {number1} & {number2} is ',div_numbers)

if __name__ == '__main__':
    main()
    