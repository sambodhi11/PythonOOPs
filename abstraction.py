from abc import ABC, abstractmethod
class Shape(ABC):
    def check(self,x):
        print("Shape: ", x)
    @abstractmethod
    def task(self):
        print("Inside Class Shape.")
 
class Square(Shape):
    def task(self):
        print("Square")
 
class Rectangle(Shape):
    def task(self):
        print("Rectangle")
        
Squ = Square()
Squ.task()
Squ.check(100)
Rect = Rectangle()
Rect.task()
Rect.check(200)
 
print("Instance:", isinstance(Squ, Shape))
print("Instance:", isinstance(Rect, Shape))
