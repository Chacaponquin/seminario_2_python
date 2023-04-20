from src.classes.Point import Point
import math


class Rectangle:
    def __init__(self, point_one: Point, point_two: Point):
        self.point_one = point_one
        self.point_two = point_two

    # método constructor para crear los puntos de la diagonal
    # en caso de no recibir parámetros se crearán ambos puntos en el origen de coordenadas
    @staticmethod
    def builder(x1=0, y1=0, x2=0, y2=0):
        return Rectangle(Point.builder(x1, y1), Point.builder(x2, y2))

    # método que muestre la base del rectángulo
    def base(self):
        b = math.sqrt(math.pow(self.point_two.x - self.point_one.x, 2))
        return b

    # método que muestre la altura del rectángulo
    def height(self):
        h = math.sqrt(math.pow(self.point_two.y - self.point_one.y, 2))
        return h

    # método que muestre el área del rectángulo
    def area(self):
        return self.base() * self.height()
