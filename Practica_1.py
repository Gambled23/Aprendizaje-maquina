var1 = input("Introduce un número: ")
var2 = input("Introduce otro número: ")

# check if it is float
try:
    var1 = int(float(var1))
    var2 = int(float(var2))
except ValueError:
    print("Los datos introducidos no son números")
    exit()

if var1 % var2 == 0:
    print("El número", var1, "es múltiplo de", var2)
else:
    print("El número", var1, "no es múltiplo de", var2)