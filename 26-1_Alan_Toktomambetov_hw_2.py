class Figure:

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

    def calculate_area(self):
        perimetr = 2 * self.__side_length
        return perimetr

    def info(self):
        print(f"Square side length: {self.__side_length}, area: {self.calculate_area()}")

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        self.__side_length = value


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        perimetr = self.__length * self.__width
        return perimetr

    def info(self):
        print(f"length: {self.__length}cm, width: {self.__width}cm, area: {self.calculate_area()}")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


square1 = Square(side_length=5)
square2 = Square(side_length=7)
rectangle1 = Rectangle(length=4, width=7)
rectangle2 = Rectangle(length=8, width=5)
rectangle3 = Rectangle(length=15, width=6)

figure = [square2, square1, rectangle1, rectangle3, rectangle2]

for figure in figure:
    figure.calculate_area()
    figure.info()
