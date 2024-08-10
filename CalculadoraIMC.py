
# Calculadora de IMC

#Evitar que se deje vacía la respuesta

def no_vacio (mensaje):
    while True:
        dato= input (mensaje)
        if dato.strip():
            return dato
        else:
            print ("Este campo no puede quedar vacío, introduce nuevamente. ")

def interpretar_imc(imc):
    if imc < 16.5:
        return ("lo que significa que tienes bajo peso severo o delgadez extrema. ")
    elif imc >=16.5 and imc <18.5:
        return ("lo que significa es que tienes bajo peso. ")
    elif imc >=18.5 and imc <25:
        return ("lo que significa que tienes peso normal. ")
    elif imc >=25 and imc <30:
        return ("lo que significa que tienes sobrepeso. ")
    elif imc >=30 and imc <35:
        return ("lo que significa es que tienes obesidad moderada o tipo I. ")
    elif imc >=35 and imc <40:
        return ("lo que significa es que tienes obesidad severa o tipo 2. ")
    elif imc >= 40:
        return ("lo que significa es que tienes obesidad mórbida o tipo 3. ")
    

# Dar la bienvenida y saludar
print ()
print (" Hola! vamos a calcular tu IMC ")
print()
print(" Vamos a necesitar unos datos... Empecemos! ")
print()

#Solicitar datos
nombre = no_vacio (" Cómo te llamas? ")

apellido_p = no_vacio (" Cuál es tu apellido paterno? ")

apellido_m = no_vacio (" Cuál es tu apellido materno? ")

edad1 = int (no_vacio (" Cuál es tu edad en años? "))
edad = abs (edad1)  # se convierte a numero positivo

peso1 = float (no_vacio (" Dime cuánto pesas (en kilos) "))
peso= abs (peso1)  # se convierte a numero positivo

talla1 = float (no_vacio (" Dime cuál es tu estatura (en metros) "))
talla = abs (talla1) # se convierte a número positivo

#Calcula el IMC
imc = peso / talla ** 2

interpretacion = interpretar_imc(imc)

#Despliega resultados
print(f"Tu nombre es {nombre.title()} {apellido_p.title()} {apellido_m.title()}, tienes {edad} años. ") #se usa title para poner siempre la primera letra en mayúscula. 
print(f"Tu Índice de masa corporal es {imc:.2f}, {interpretacion}. ") #imprime el IMC con formato de 2 decimales y la interpretación.



