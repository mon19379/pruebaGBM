def espalindromo (palabra):
   palabra = palabra.replace(" ","").lower() 
   palindromo = palabra == palabra[::-1]
   return palindromo 


