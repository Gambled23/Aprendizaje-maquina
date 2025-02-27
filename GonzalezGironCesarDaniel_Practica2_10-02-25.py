# Objetivo: Crear un programa que simule la compra de boletos de cine y aplique promociones según la edad, cantidad de boletos y hora de la función

precioBoleto = 50
edad = int(input("Por favor ingresa tu edad: "))
numeroBoletos = int(input("Por favor ingresa el numero de boletos que deseas comprar: "))
horaFuncion = int(input("Por favor ingresa la hora de la funcion (formato 24 horas): "))


total = precioBoleto * numeroBoletos

if edad < 18: # Obtener descuento por edad
    promoEdad = True
    print("Eres elegible para un 20% de descuento por ser menor de 18 años")
    total = total - (total * 0.2)

if numeroBoletos > 4: # Obtener descuento por más de 4 boletos
    promoNumeroBoletos = True
    print("Eres elegible para un 10% de descuento por comprar mas de 4 boletos")
    total = total - (total * 0.1)

if horaFuncion < 15: # Obtener descuento por función matine
    promoMatine = True
    print("Eres elegible para un 15% de descuento por comprar boletos para una funcion antes de las 3:00 pm")
    total = total - (total * 0.15)

input("Presiona enter para continuar")
print("El total a pagar es de: $", total)

if numeroBoletos > 6 and (horaFuncion < 15 or edad < 18): # Obtener snack gratis si aplica
    print("Por la acumulación de promociones, puedes disfrutar de un snack gratis, pasa a dulcería a recogerlo")
else:
    print("No eres elegible para un snack gratis, lo lamentamos")