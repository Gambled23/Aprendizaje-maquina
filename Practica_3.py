num = 0

while True:
  print("1- Sumar\n 2- Restar\n 3- Multiplicar\n 4- Dividir\n 5. Salir")
  num = int(input("Elige una opcion: "))
  if num==1:
    num = int(input("Numero: "))
    num += int(input("Otro número: "))
  elif num==2:
    num = int(input("Numero: "))
    num -= int(input("Otro número: "))
  elif num==3:
    num = int(input("Numero: "))
    num *= int(input("Otro número: "))
  elif num==4:
    num = int(input("Numero: "))
    num /= int(input("Otro número: "))
  elif num==5:
    break
  else:
    print("Opción no valida")
    continue
  print("Resultado: ", num)