# # Написать класс Vector с двумя полями x и y типа инт
#
# # Реализовать возможность сложения двух объектов класса Vector через оператор сложения "+" | x1 + x2 ; y1 + y2
#
# # В результате сложения получается новый объект класса Vector

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(x=1, y=1)
v2 = Vector(x=4, y=-5)
v3 = v1 + v2

print(f'\nРезультирующий вектор: x={v3.x}, y={v3.y}\n')
assert v3.x == 5
assert v3.y == -4
