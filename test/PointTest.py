import sys
import unittest

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


if __name__ == '__main__':
	unittest.main()
