class Calculator:
    num = 100  # class variable, it will be constant no matter how many object you create

    # But Instance variable will defer for each and every object

    # default constructor - name should be __init__
    # constructor is a method automatically called when you create object for class

    # self keyword is mandatory for calling variable into method
    # new keyword is not required when you create object

    def __init__(self, a, b):
        self.firstNumber = a  #these are instance variables, keep on changing for every object creation
        self.secondNumber = b
        print("calling default constructor method")

    # Self parameter in mandatory when declaring the variable inside the class
    def getData(self):
        print("executing method in a class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # Can create n no. of object like obj, obj1
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)  # Can create n no. of object like obj, obj1
obj1.getData()
print(obj1.summation())
