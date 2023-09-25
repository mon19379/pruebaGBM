import unittest
from Ejercicio1 import espalindromo

class test(unittest.TestCase):
    def test_palindromo1(self):
        self.assertTrue(espalindromo("Ana"))  
    
archivo = open("Output1.txt","w")
archivo.write(str(espalindromo("Ana")))
    
    
if __name__ == '__main__':
    unittest.main()