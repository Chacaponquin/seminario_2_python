from src.utils import show_success
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Método estático de la clase que permite crear puntos fácilmente,
    # en el caso de no recibir parámetros el punto estará situado en el origen de coordenadas
    @staticmethod
    def builder(x=0, y=0):
        return Point(x, y)

    # Se sobreescribe el método string para mostrar las coordenadas del punto de la forma (X,Y)
    def __str__(self):
        return "(" + f"{self.x}" + "," + f"{self.y}" + ")"

    # Se sobreescribe el método equal para poder comparar dos puntos a partir de sus coordenadas
    def __eq__(self, point_2):
        return self.x == point_2.x and self.y == point_2.y

    # El método quadrant() determina y muestra el cuadrante en el que se encuentra el punto
    def quadrant(self):
        cuadrante = ''
        if self.x == 0 and self.y != 0:
            cuadrante = "El punto se encuentra sobre el eje X"
        elif self.y == 0 and self.x != 0:
            cuadrante = "El punto se encuentra sobre el eje Y"
        elif self.x > 0:
            if self.y > 0:
                cuadrante = "El punto se encuentra en el primer cuadrante"
            else:
                cuadrante = "El punto se encuentra en el cuarto cuadrante"
        elif self.x < 0:
            if self.y > 0:
                cuadrante = "El punto se encuentra en el segundo cuadrante"
            else:
                cuadrante = "El punto se encuentra en el tercer cuadrante"
        else:
            cuadrante = "El punto se encuentra en el origen de coordenadas"

        return cuadrante

    # El método vector(point) devuelve el vector resultante entre el punto y otro punto
    def vector(self, point):
        return Point(self.x-point.x, self.y-point.y)

    # El método distance(point) devuelve la distancia entre el punto y otro punto
    def distance(self, point):
        vector = self.vector(point)
        return math.sqrt(math.pow(vector.x, 2) + math.pow(vector.y, 2))










