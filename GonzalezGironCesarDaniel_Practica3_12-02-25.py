#Objetivo: Calculadora básica con suma, resta, multiplicación, división y exponente que utilice solo una variable
num = 0

while True: #Menu infinito
  print("1- Sumar\n2- Restar\n3- Multiplicar\n4- Dividir\n5- Exponente\n6- Salir")
  num = int(input("Elige una opcion: "))
  if num==1: # Sumar
    num = int(input("Numero 1: "))
    num += int(input("Numero 2: "))
  elif num==2: # Restar
    num = int(input("Numero 1: "))
    num -= int(input("Numero 2: "))
  elif num==3: # Multiplicar
    num = int(input("Numero 1: "))
    num *= int(input("Numero 2: "))
  elif num==4: # Dividir
    num = int(input("Numero 1: "))
    num /= int(input("Numero 2: "))
  elif num==5: # Exponente
    num = int(input("Numero 1: "))
    num **= int(input("Numero 2: "))
  elif num==6: # Salir
    break
  else: # Opción no válida
    print("La opción no existe")
    continue
  print("Resultado: ", num)