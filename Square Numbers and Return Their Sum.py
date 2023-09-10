# Challenge 1: Square Numbers and Return Their Sum
# Create a class `Point` with three properties: `x`, `y`, and `z`.
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        if (self.x == self.y == self.z):
            sum_squares = (self.x**2)*3
            return sum_squares
        else: 
            sum_squares = self.x**2 + self.y**2 + self.z**2
            return sum_squares

if __name__ == '__main__':
    number1 = int(input('enter a number1: '))
    number2 = int(input('enter a number2: '))
    number3 = int(input('enter a number3: '))
    obj_point = Point(number1,number2,number3)
    sq_sum = obj_point.sqSum()
    print(f'Sum of squares of {number1}, {number2} & {number3}: ',sq_sum)
