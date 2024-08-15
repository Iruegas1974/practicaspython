# ###errores: 
# # 1. sintaxis (de dedo) 

# # 2. Errores en tiempo de ejecucion: 
# # se debe a fala de validacion de un dato por parte del programador, 
# # a la inexistencia de un dato (que este sea nulo), etc. 
# # Ejemeplo: 

# numHuevos = 12
# #print("Tengo " + numHuevos + " huevos.")  # error

# # Opción 1 de resolver el error
# print("Tengo " + str(numHuevos) + " huevos")

# # Opción 2
# print("Tengo %s huvos." %(numHuevos))

# # 3. Error de lógica: Los dos errores anteriores impediràn la ejecución del programa, 
# # pero un error en la lógica de programación no. Este simplemente mostraría un resultado no deseado.

# # Calcular la superficie o área de un cuadrado

# lado = int(input("Ingresa la medida del lado del cuadrado: "))
# superficie = lado *lado * lado # la formula esta mal.
# print("La superficie del cuadrado es: " + str(superficie))
# # se soluciona sabiendo la fórmula.

# Módulo 1, semana 4 ejercicio.py (Llenar un formulario)

nombre= input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
correo = input("Introduce tu correo electrónico: ")
telefono = input("Introduce tu teléfono: ") # Se deja en str porque si empieza con "0" desaparecerìa si lo pasamos a int

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Tengo " + str(edad) + " años.")
print("Correo: " + correo)
print("Teléfono: " + telefono)