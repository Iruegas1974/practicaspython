# Calculadora de IMC  

# Da la bienvenida y saludar
print ()
print (" Hola! vamos a calcular tu IMC ")
print()
print(" Vamos a necesitar unos datos... Empecemos! ")
print()

# Pregunta el nombre, asegura que no quede vacìo
while True: 
    nombre = input (" Ingresa tu nombre: ")
    if nombre.strip():
        break
    else: 
        print("El nombre no puede quedar vacío, inténtalo de nuevo: ")

# Pregunta el apellido paterno, asegura que no quede vacío
while True:
    apellido_p = input (" Ingresa tu apellido paterno: ")
    if apellido_p.strip():
        break
    else:
        print("El apellido paterno no puede quedar vacío, inténtalo de nuevo: ")

# Pregunta el apellido materno, asegura que no quede vacío
while True:
    apellido_m = input (" Ingresa tu apellido materno: ")
    if apellido_m.strip():
        break
    else: 
        print("El apellido materno no puede quedar vacío, inténtalo de nuevo: ")

# Pregunta la edad, asegura rango aceptable y que no quede vacío
while True:
    try:
        edad = int (input (" Cuál es tu edad en años? "))
        if 1 <= edad <= 100:
            break
        else: 
            print ("La edad debe estar entre 1 y 100 años. ")
    except ValueError:
        print ("Debes ingresar un número válido para la edad. ")

# Pregunta el peso, asegura rango aceptable y que no quede vacío
while True:
    try:
        peso = float (input (" Dime cuánto pesas (en kilos) "))
        if 1<= peso <=400:
            break
        else: 
            print ("El peso debe estar entre 1 y 400 kg")
    except ValueError:
        print("Debes ingresar un número válido para el peso. ")

# Pregunta la talla, asegura rango aceptable y que no quede vacío
while True:
    try:
        talla = float (input (" Dime cuál es tu estatura (en metros) "))
        if 0.5<= talla <=2.5:
            break
        else:
            print("La talla debe estar entre 0.5 y 2.5 metros. ")
    except ValueError:
        print("Debes ingresar un número válido para la talla. ")

# Calcula el IMC
imc = peso / talla ** 2

# interpreta el IMC
if imc < 16.5:
    interpretacion = "lo que significa que tienes bajo peso severo o delgadez extrema. "
elif imc >=16.5 and imc <18.5:
    interpretacion = "lo que significa es que tienes bajo peso. "
elif imc >=18.5 and imc <25:
    interpretacion = "lo que significa que tienes peso normal. "
elif imc >=25 and imc <30:
    interpretacion = "lo que significa que tienes sobrepeso. "
elif imc >=30 and imc <35:
    interpretacion = "lo que significa es que tienes obesidad moderada o tipo I. "
elif imc >=35 and imc <40:
    interpretacion = "lo que significa es que tienes obesidad severa o tipo 2. "
elif imc >= 40:
    interpretacion = "lo que significa es que tienes obesidad mórbida o tipo 3. "
    
#Despliega resultados
print()
print(f"Tu nombre es {nombre.title()} {apellido_p.title()} {apellido_m.title()}, tienes {edad} años. Tu peso es {peso} kilos y mides {talla} metros.") #se usa title para poner siempre la primera letra en mayúscula. 
print()
print(f"Tu Índice de masa corporal es {imc:.2f}, {interpretacion} ") #imprime el IMC con formato de 2 decimales y la interpretación.
print()