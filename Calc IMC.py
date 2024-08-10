# Calculadora de índice de masa corporal

# Método para que no queden campos vacíos al solicitar datos

def solicitar_dato(mensaje):
     while True:
          dato= input (mensaje)
          if dato.strip():
               return dato
          else:
               print("Este campo no puede estar vacío. Inténtalo de nuevo.")

# Método para que sean valores factibles (enteros)
def rango_correcto_edad(mensaje):
    while True:
        dato= int (input(mensaje))
        if dato > 0 and dato <=100:
            return dato
        
def rango_correcto_peso(mensaje):
    while True:
        dato= float (input(mensaje))
        if dato > 0 and dato <=500:
            return dato
            
def rango_correcto_talla(mensaje):
    while True:
        dato=float(input(mensaje))
        if dato >1.0 and dato <= 2.5:
            return dato
        
# Método para calcular el IMC
def calcular_IMC(peso,talla):
     return (peso/(talla**2))

# Método para la interpretación del IMC
def interpretar_IMC(IMC):
    if IMC < 16.5:
        return ("lo que significa que tienes bajo peso severo o delgadez extrema. ")
    elif IMC >=16.5 and IMC <18.5:
        return ("lo que significa es que tienes bajo peso. ")
    elif IMC >=18.5 and IMC <25:
        return ("lo que significa que tienes peso normal. ")
    elif IMC >=25 and IMC <30:
        return ("lo que significa que tienes sobrepeso. ")
    elif IMC >=30 and IMC <35:
        return ("lo que significa es que tienes obesidad moderada o tipo I. ")
    elif IMC>=35 and IMC <40:
        return ("lo que significa es que tienes obesidad severa o tipo 2. ")
    elif IMC >= 40:
        return ("lo que significa es que tienes obesidad mórbida o tipo 3. ")
    
# Saludo inicial
print()
print("Hola, vamos a calcular tu Índice de masa corporal")
print()
print("Vamos a necesitar algunos datos. Iniciemos ... ")
print()

# Solicitamos el nombre 
nombre = solicitar_dato("1. Cuál es tu nombre?  ")
 
# Solicitamos el apellido paterno
apellidoP = solicitar_dato("2. Cuál es tu apellido paterno? ")

# Solicitamos el apellido materno
apellidoM = solicitar_dato("3. Cuál es tu apellido materno? ")
 
# Solicitamos su edad, variable entera porque es en años
edad1 = int(solicitar_dato("4. Cuál es tu edad? "))
edad = abs (edad1) # cambio a positivo cualquier número negativo 
edad = rango_correcto_edad(mensaje= "El rango es incorrecto, introduce un número entre 1 y 100 años: ")

# Solicitamos su peso en kilogramos, variable flotante porque puede tener decimales
peso1 = float (solicitar_dato("5. Dime cual es tu peso en kilogramos "))
peso = abs (peso1) # cambio a positivo cualquier número negativo
peso = rango_correcto_peso(mensaje="El rango es incorrecto, introduce un número entre 1 y 500 kg: ")

# solicitamos su talla, en metros, variable flotante porque tiene punto decimal
talla1 = float (solicitar_dato("6. Ahora dime cual es tu estatura en metros "))
talla = abs(talla1) # cambio a positivo cualquier número negativo
talla = rango_correcto_talla(mensaje="EL rango es incorrecto, introduce un número entre 1.00 y 2.50 metros: ")

 
IMC = calcular_IMC ( peso, talla)
interpretacion = interpretar_IMC(IMC)

print()
# Se despliega el nombre del sujeto y la edad
# Se utiliza el método title() para cambiar la capitalidad de las letras (se escribiran con la primera en mayúscula)
print (nombre.title() + " " + apellidoP.title()+ " " + apellidoM.title() + " tienes " + str(edad) + " años") 

# Verificamos si es menor o mayor de edad
if edad < 18:
    print ("Por lo tanto eres menor de edad.")
else:
    print ("Por lo tanto eres mayor de edad.")

# Se despliega el peso, la talla, IMC e interpretaciòn. 
print (f"Con tu peso de {peso} kg. y tu estatura de {talla} metros, ")
print (f"Tienes un Índice de Masa Corporal de {IMC:.2f} kg/m2, {interpretacion}")
print()


                                               