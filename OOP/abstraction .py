from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side **2
    def perimeter(self):
        return self.__side *4
class React(Shape):
    def __init__(self,length , width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return (self.__width + self.__length ) * 2        

def main():
    square_1 = Square(10)
    print(f"square area is {square_1.area()} and perimeter is {square_1.perimeter()}")
    rect_1 = React(5,3)
    print(f"rectangle area is {rect_1.area()} and perimeter {rect_1.perimeter()}")


if __name__ == '__main__':
    main()