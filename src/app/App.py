

from src.classes import Point, Rectangle
from rich.table import Table
from rich.console import Console
from src.utils import show_success


class App:
    def __init__(self):
        # crear los puntos a, b, c y d
        self.point_a, self.point_b, self.point_c, self.point_d = self.create_points()
        # crear rectangulo de los ejercicos 6 y 7
        self.rectangle = self.create_rectangle(self.point_a, self.point_b)

    def start(self):
        self.ex1()
        self.ex2()
        self.ex3()
        self.ex4()
        self.ex5()
        self.ex7()

    def ex7(self):
        table = Table(border_style="green")

        table.add_column("Dato", style="green", no_wrap=True)
        table.add_column("Valor", style="green", no_wrap=True)

        table.add_row('Base', str(self.rectangle.base()))
        table.add_row('Altura', str(self.rectangle.height()))
        table.add_row('Área', str(self.rectangle.area()))

        self.print_table(table)

    def ex5(self):
        # crear punto (0, 0)
        point_initial = Point.builder()

        # calcular la distancia con cada punto
        distance_a_initial = point_initial.distance(self.point_a)
        distance_b_initial = point_initial.distance(self.point_b)
        distance_c_initial = point_initial.distance(self.point_c)

        # sacar cual es la distancia máxima
        max_distance = max(distance_a_initial, distance_b_initial, distance_c_initial)

        # ver cuál es el punto de mayor distancia
        point = ''
        if max_distance == distance_a_initial:
            point = 'A'
        elif max_distance == distance_b_initial:
            point = 'B'
        else:
            point = 'C'

        # crear tabla
        table = Table(border_style="green")

        table.add_column("Punto", style="green", no_wrap=True)
        table.add_column("Distancia con el punto (0, 0)", style="green", no_wrap=True)

        table.add_row('A', str(distance_a_initial))
        table.add_row('B', str(distance_b_initial))
        table.add_row('C', str(distance_c_initial))

        # mostrar tabla
        self.print_table(table)
        # mostrar cuál es la distancia mayor
        show_success(f'El punto con mayor distancia con respecto al punto (0, 0) es: {point}')

    def ex4(self):
        table = Table(border_style="green")

        table.add_column("Puntos", style="green", no_wrap=True)
        table.add_column("Distancia entre los puntos", style="green", no_wrap=True)

        table.add_row('A -> B', str(self.point_a.distance(self.point_b)))
        table.add_row('B -> A', str(self.point_b.distance(self.point_a)))

        self.print_table(table)

    def ex3(self):
        table = Table(border_style="green")

        table.add_column("Vector", style="green", no_wrap=True)
        table.add_column("Valor", style="green", no_wrap=True)

        table.add_row('AB', str(self.point_a.vector(self.point_b)))
        table.add_row('BA', str(self.point_b.vector(self.point_a)))

        self.print_table(table)

    def ex2(self):
        table = Table(border_style="green")

        table.add_column("Punto", style="green", no_wrap=True)
        table.add_column("Cuadrante", style="green", no_wrap=True)

        table.add_row('A', self.point_a.quadrant())
        table.add_row('C', self.point_c.quadrant())
        table.add_row('D', self.point_d.quadrant())

        self.print_table(table)

    def ex1(self):
        table = Table(border_style="green")

        table.add_column("Punto", style="green", no_wrap=True)
        table.add_column("X", style="green", no_wrap=True)
        table.add_column("Y", style="green", no_wrap=True)

        table.add_row('A', str(self.point_a.x), str(self.point_a.y))
        table.add_row('B', str(self.point_b.x), str(self.point_b.y))
        table.add_row('C', str(self.point_c.x), str(self.point_c.y))
        table.add_row('D', str(self.point_d.x), str(self.point_d.y))

        self.print_table(table)

    def create_points(self):
        point_a = Point.builder(2, 3)
        point_b = Point.builder(5, 5)
        point_c = Point.builder(-3, -1)
        point_d = Point.builder(0, 0)

        return point_a, point_b, point_c, point_d

    def create_rectangle(self, point1: Point, point2: Point):
        return Rectangle.builder(point1.x, point1.y, point2.x, point2.y)

    def print_table(self, table: Table):
        console = Console()
        console.print(table)


if __name__ == '__main__':
    App().start()