import unittest
from utilidades import calcular_iva

#Establece caso de test
class test_calcular_iva(unittest.TestCase):
    def test_calcular_iva(self):
        #Llama a la función
        self.assertEqual(calcular_iva(100), 21)

#Flujo desde principio
if __name__ == '__main':
    unittest.main()