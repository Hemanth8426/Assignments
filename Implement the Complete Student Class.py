# Challenge 3: Implement the Complete Student Class 
# Implement the complete **Student** class according to the rules of encapsulation 
# by using getName, setName, getRollNumber,setRollNumber

class Student:
    
    def set(self,name,roll_num):
        self.set_name(name)
        self.set_roll_num(roll_num)
    
    def display(self):
        # accessing private methods
        self.__get_name()
        self.__get_roll_num()
        
    def set_name(self,name):
        self.__name = name # created private variable
    
    def __get_name(self): # created private method
        print('Student name is ',self.__name)  # accessed private variable
        
    def set_roll_num(self,roll_num):
        self.__roll_num = roll_num # created private variable
    
    def __get_roll_num(self): # created private method
        print('Student roll number is ',self.__roll_num) # accessed private variable
    
if __name__ == '__main__':
    std = Student()
    std.set('Raghu',56849)
    std.display()
    std.set('Vijay',59876)
    std.display()
