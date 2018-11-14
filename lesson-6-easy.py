# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Figure:
    def __side_length(self, x2, x1, y2, y1):
        return round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = self.__side_length(x2, x1, y2, y1)
        self.b = self.__side_length(x3, x2, y3, y2)
        self.c = self.__side_length(x1, x3, y1, y3)

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def square(self):
        p = self.perimeter()
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def height(self):
        s = self.square()
        return round(2 * s / self.a, 2)
    

triangle = Figure(2, 1, 1, -2, -1, 0)
print(triangle.height(), triangle.perimeter(), triangle.square())    


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __side_length(self, x2, x1, y2, y1):
        return round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.a = self.__side_length(x2, x1, y2, y1)
        self.b = self.__side_length(x3, x2, y3, y2)
        self.c = self.__side_length(x4, x3, y4, y3)
        self.d = self.__side_length(x1, x4, y1, y4)

    def is_isosceles(self):
        self.d1 = math.sqrt(self.a * self.b + (self.d**2) + self.b * ((self.c**2) - (self.d**2))/self.b-self.a)
        self.d2 = math.sqrt(self.a * self.b + (self.c**2) - self.b * ((self.c**2) - (self.d**2))/self.b-self.a)
        if self.d1 == self.d2:
            print("Трапеция равнобедренная")

    def perimeter(self):
        return (self.a + self.b + (2 * self.c))

    def square(self):
        s = self.perimeter() / 2
        return round(math.sqrt((s - self.a) * (s - self.b) * (s - self.c) * (s - self.c)), 2)