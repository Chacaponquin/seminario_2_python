from src.utils import show_success
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Se sobreescribe el método string para mostrar las coordenadas del punto de la forma (X,Y)
    def __str__(self):
        return "(" + f"{self.x}" + "," + f"{self.y}" + ")"
    # El método quadrant() determina y muestra el cuadrante en el que se encuentra el punto
    def quadrant(self):
        if self.x == 0 and self.y != 0:
            print("El punto " + self.__str__() + " se encuentra sobre el eje X")
        elif self.y == 0 and self.x != 0:
            print("El punto " + self.__str__() + " se encuentra sobre el eje Y")
        elif self.x > 0:
            if self.y > 0:
                print("El punto " + self.__str__() + " se encuentra en el primer cuadrante")
            else:
                print("El punto " + self.__str__() + " se encuentra en el cuarto cuadrante")
        elif self.x < 0:
            if self.y > 0:
                print("El punto " + self.__str__() + " se encuentra en el segundo cuadrante")
            else:
                print("El punto " + self.__str__() + " se encuentra en el tercer cuadrante")
        else:
            print("El punto " + self.__str__() + " se encuentra en el origen de coordenadas")

    # El método vector(point) devuelve el vector resultante entre el punto y otro punto
    def vector(self, point):
        return Point(self.x-point.x, self.y-point.y)

    # El método distance(point) devuelve la distancia entre el punto y otro punto
    def distance(self, point):
        vector = self.vector(point)
        return math.sqrt(math.pow(vector.x, 2) + math.pow(vector.y, 2))










