# Operadores aritmèticos
# print (2 + 2) # suma
# print(4 - 2) # resta
# print(3 * 7) # multiplicación
# print(15 / 2) # división
# print(11 % 4) # módulo, se lee "11 módulo 4" da el residuo (lo que sobra de la división)
# print(11 // 4) # división de piso, el resultado es el resultado entero de la división 
# print(2 ** 3) # potencia

# # Operadores en cadenas de texto 
# print("Hola " + "Mundo")  # concatenación
# print("Hola "* 3) # repetición 
# print(("Hola " + "mundo ") * 3) # concatenacion y repetición 

# Operadores de comparación (responde verdadero o falso)
# print("Hola" == "hola") # igual que 
# print("Hola" != "hola") # distinto qu 
# print(3 < 11) # menor que
# print(10 <= 10) # menor o igual que
# print(10 > 10) # mayor que 
# print(3 >= 11) # mayor o igual que 

# Operadores de existencia (si un elemento existe dentro de otro elemento)
# print ("ola" in "Hola")   # existencia: si ola esta en Hola  (True)
# print ("ola" not in "Hola") # inexistencia: si ola no esta en Hola (False)

# Operadores booleanos
# print(True or False) # una de las 2 debe ser true
# print(True and False) # las dos deben ser true verifica que se cumplan las 2 condiciones

# # Operadores de asignación
# x = 1   # se asigna el valor 1 a la variable x
# x += 2   #x + 2 va a ser x=3 (operador de asignaciòn suma`)
# x *= 3 # x que es 3 multiplicado por 3 (operador de asignación de multiplicación)
# x %= 4 # x que es 9 dividido entre 4  y el residuo es 1 (operador de asignación de mòdulo `)
# print(x)  # imprimira el resultado de x=1

# JERARQUIA DE OPERACIONES

# 1. Paréntesis 
# 2. Exponentes
# 3. Multiplicacion, division, modulo, division de piso 
# 4. sumas y restas 
# 5. Si hay dos de la misma jerarquia se priorizan de izquierda a derecha

x = 6 * 5 + 8 / 2 ** 4
print(x)
