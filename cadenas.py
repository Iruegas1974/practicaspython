# texto_variado = "Palabra 123 +- * ·%&"
# print (type(texto_variado))

# # podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print ("""
# Funcionamiento de \
# programa: (opciones)
#     - 1 Para acceder a opciones
#     - 2 para salir           
#        """)

##################################################
# subscripting e indexado (indices empiezan en 0,)

# texto = "Python"

# print(texto[0]) # imprime la P
# print(texto[5]) # imprime n
# print(texto[-1]) # imprime n
# print(texto[-6]) # imprime P

# print(texto[6]) # error, no podemos acceder a una posición que no existe
# print(texto[-7]) # error, no podemos acceder a una posición que no existe

# letra = texto[0]
# print (letra)

# # texto[0]="p"  # error no podemos modificar una cadena 

# letra = "p"
# print (letra)

# texto_compuesto=letra + texto[1]
# print (texto_compuesto)

###########################

#slicing o substringing
#texto = "Python"
# print (texto[0:3])   # el ultimo elemento es menos uno (se imprimira el 0, 1 y 2)
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:]) # que imprima del 2 al final 
# print(texto[:3]) # que imprima hasta el 2

# print(texto[-3::-1]) # imprime al reves: htyP
#print(texto[::-1]) # escribe Python al reves
#print(texto[1:50])
#print(texto[2:2])  # no se escribe nada porque el ultimo no se escribe y es el mismo que el de inicio 

###############################################################

#cadenas y formatos

# texto = "Hola mundo! Buenastardes"
# print(texto.lower())  # todo en minúsculas
# print(texto.upper()) # todo en mayúsculas
# print(texto.capitalize()) # la primera letra de la oración se vuelve mayuscula
# print(texto.title()) # la primera letra de cada palabra es mayuscula
# print(texto.swapcase()) # la primeras letras de cada frase se vuelven minusculas y el resto mayusculas

# texto = texto.upper()
# print(texto)

# cadenas formateadas
print("{} + {} = {}". format(2,3, 2+3))
print("{} + {} = {}". format("Hola", "Mundo", "Hola Mundo"))
print("{:.3f} + {:.4f} = {}". format(2,3,2+3))  # flotante con decimales
print("{1} + {0} = {2}". format(2,3,2+3)) # cambiamos el orden 
print("{2} + {0} = {1}". format("Hola", "Mundo", "Hola Mundo")) # cambiamos el orden 
print("{:d} = {:b} = {:o} = {:x}". format(15,15,15,15)) # solicitamos decimal, binario, octadecimal, hexadecimal

# para buscar mas metodos de str, 
# en la terminal escribir Pyton
# luego dir(str) y aparecen todos los mètodos.