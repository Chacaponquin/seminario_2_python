import sys
import unittest
import math

# esto se hace para poder acceder a los módulos dentro de la carpeta src
sys.path.append('./')

from src.classes import Point


# clase para los tests correspondientes a la clase Point
class PointTest(unittest.TestCase):
	# test para verificar si se esta creando el punto con las coordenadas correctas
	def testCreatePointTest(self):
		point = Point(5, 4)

		correct_cord_x = point.x == 5
		correct_cord_y = point.y == 4

		# esto verifica que la coordenada x sea igual a 5 y la coordenada y sea igual a 4
		# sirve para comprobar que en el constructor se inicializan bien las variables

		are_correct = bool(correct_cord_x and correct_cord_y)
		self.assertTrue(are_correct)

	# test para verificar que en el caso de no recibir parámetros las coordenadas sean (0,0)
	def test_create_point_test_2(self):
		point = Point()

		correct_cord_x = point.x == 0
		correct_cord_y = point.y == 0

		are_correct = bool(correct_cord_x and correct_cord_y)
		self.assertTrue(are_correct)

	# test para verificar que el vector calculado entre dos puntos sea el correcto
	def test_vector(self):
		point = Point(8, 3)
		point_2 = Point(6, 2)

		self.assertEqual(point.vector(point_2), Point(2, 1))

	# test para verificar que la distancia calculada entre dos puntos sea correcta
	def test_distance(self):
		point = Point(8, 3)
		point_2 = Point(6, 2)

		v_x = point.x - point_2.x
		v_y = point.y - point_2.y

		correct_distance = math.sqrt(math.pow(v_x, 2) + math.pow(v_y, 2))
		self.assertEqual(point.distance(point_2), correct_distance)


if __name__ == '__main__':
	unittest.main()
