import unittest
from Ejercicio1 import espalindromo

class test(unittest.TestCase):
    def test_palindromo1(self):
        self.assertTrue(espalindromo("Francisco"))  

archivo = open("Output2.txt","w")
archivo.write(str(espalindromo("Francisco")))
    

if __name__ == '__main__':
    unittest.main()