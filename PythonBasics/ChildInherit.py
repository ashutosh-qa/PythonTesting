# Below is the format to import, here OOPs is file name and Calculator is the class
from PythonBasics.OOPs import Calculator


class childInherit(Calculator):
    num2 = 200

    # below is the format to call Parent class constructor
    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = childInherit()
print(obj.getCompleteData())