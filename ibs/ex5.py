# # Написать абстрактный класс "Figure", в котором содержится пустой метод calc_area()
#
# # Написать классы "Square", "Circle", которые наследуются и переопределяют метод calc_area() для каждой фигуры
#
# # Класс "Square" имеет поле side (сторона) типа int
#
# # Класс "Circle" имеет поле radius (радиус) типа int

from math import pi


class Figure:
    def calc_area(self):
        pass


class Square(Figure):

    def __init__(self, side: int):
        self.side = side

    def calc_area(self):
        return self.side ** 2


class Circle(Figure):

    def __init__(self, radius: int):
        self.side = radius

    def calc_area(self):
        return pi * self.side ** 2


square = Square(side=4)
circle = Circle(radius=3)

print(f'Площадь Квадрата={square.calc_area()}\nПлощадь Круга={circle.calc_area()}')
assert square.calc_area() == 16, 'Неверно посчитана площадь квадрата!'
assert circle.calc_area() == 28.274333882308138, 'Неверно посчитана площадь круга!'
