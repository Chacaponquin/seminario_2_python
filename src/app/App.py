from src.classes import Point, Rectangle
from src.utils import show_success, define_table, define_table_column, print_table


class App:
    def __init__(self):
        # crear los puntos a, b, c y d
        self.point_a, self.point_b, self.point_c, self.point_d = self.create_points()
        # crear rectangulo de los ejercicos 6 y 7
        self.rectangle = self.create_rectangle(self.point_a, self.point_b)

    def start(self):
        self.show_ex_label(1)
        self.ex1()
        self.show_ex_label(2)
        self.ex2()
        self.show_ex_label(3)
        self.ex3()
        self.show_ex_label(4)
        self.ex4()
        self.show_ex_label(5)
        self.ex5()
        self.show_ex_label(7)
        self.ex7()

    def show_ex_label(self, ex_number: int):
        print(f'\n>>> Ejercicio {str(ex_number)}:')

    def ex7(self):
        table = define_table()

        define_table_column(table, 'Dato')
        define_table_column(table, 'Valor')

        table.add_row('Base', str(self.rectangle.base()))
        table.add_row('Altura', str(self.rectangle.height()))
        table.add_row('Área', str(self.rectangle.area()))

        print_table(table)

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
        table = define_table()

        define_table_column(table, 'Punto')
        define_table_column(table, 'Distancia con el punto (0, 0)')

        table.add_row('A', str(distance_a_initial))
        table.add_row('B', str(distance_b_initial))
        table.add_row('C', str(distance_c_initial))

        # mostrar tabla
        print_table(table)
        # mostrar cuál es la distancia mayor
        show_success(f'El punto con mayor distancia con respecto al punto (0, 0) es: {point}')

    def ex4(self):
        table = define_table()

        define_table_column(table, 'Puntos')
        define_table_column(table, 'Distancia entre los puntos')

        table.add_row('A -> B', str(self.point_a.distance(self.point_b)))
        table.add_row('B -> A', str(self.point_b.distance(self.point_a)))

        print_table(table)

    def ex3(self):
        table = define_table()

        define_table_column(table, 'Vector')
        define_table_column(table, 'Valor')

        table.add_row('AB', str(self.point_a.vector(self.point_b)))
        table.add_row('BA', str(self.point_b.vector(self.point_a)))

        print_table(table)

    def ex2(self):
        table = define_table()

        define_table_column(table, 'Punto')
        define_table_column(table, 'Cuadrante')

        table.add_row('A', self.point_a.quadrant())
        table.add_row('C', self.point_c.quadrant())
        table.add_row('D', self.point_d.quadrant())

        print_table(table)

    def ex1(self):
        table = define_table()

        define_table_column(table, 'Punto')
        define_table_column(table, 'X')
        define_table_column(table, 'Y')

        table.add_row('A', str(self.point_a.x), str(self.point_a.y))
        table.add_row('B', str(self.point_b.x), str(self.point_b.y))
        table.add_row('C', str(self.point_c.x), str(self.point_c.y))
        table.add_row('D', str(self.point_d.x), str(self.point_d.y))

        print_table(table)

    def create_points(self):
        point_a = Point.builder(2, 3)
        point_b = Point.builder(5, 5)
        point_c = Point.builder(-3, -1)
        point_d = Point.builder(0, 0)

        return point_a, point_b, point_c, point_d

    def create_rectangle(self, point1: Point, point2: Point):
        return Rectangle.builder(point1.x, point1.y, point2.x, point2.y)


if __name__ == '__main__':
    App().start()