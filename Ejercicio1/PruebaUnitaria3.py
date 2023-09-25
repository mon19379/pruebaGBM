import unittest
from Ejercicio1 import espalindromo

class test(unittest.TestCase):
    def test_palindromo1(self):
        self.assertTrue(espalindromo("Ale Urruela"))  
    
archivo = open("Output3.txt","w")
archivo.write(str(espalindromo(input("Ingrese palabra o frase:"))))
    

if __name__ == '__main__':
    unittest.main()