numero = "147"
print(numero)
print(type(numero))

numero = int(numero) # Cast de str a int
print(numero)
print(type(numero))

numero = float(numero) #Cast de int a float
print(numero)
print(type(numero))

numero = complex(numero) #Cast de float a completo
print(numero)
print(type(numero))

# # no se puede cambiar la letra b a un valor numerico
# numero = "b"
# numero = int(numero) #error
# print (numero)
# print(type(numero))

bandera = 0  # 0 es falso/ 1=cierto 
print(bandera)
print(type(bandera))
bandera = bool(bandera)
print(bandera)
print(type(bandera))

# REGLAS PARA NOMBRAR VARIABLES.
# variables no comienzan con numero, si puede empezar con guion bajo , 
# por buena practica el guion bajo se utiliza para separar palabras  nuevo_numero (p ejem). 
# No utilizar palabras reservadas. 
# Las variables son sensitivas a mayusculas y minusculas. 
# No se usan mayusculas (por convención)
# SERPIENTE: numero_nuevo
# CAMELLO: numeroNuevo, numeroDos

#Palabras reservadas: 
help("keywords")

