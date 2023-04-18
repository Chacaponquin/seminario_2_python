import sys
import unittest

# esto se hace para poder acceder a los módulos dentro de la carpeta src
sys.path.append('./')

from src.classes import Rectangle

# clase para los tests correspondientes a la clase Rectangle
class RectangleTest(unittest.TestCase):
    # test de prueba
    def test_example(self):
        # eso verifica si la suma entre 5 y 5 espera que de como resultado 10
        # si cumple pasará el test
        # en caso contrario lanzará un error
        self.assertEqual(5 + 5, 10)


if __name__ == '__main__':
    unittest.main()
