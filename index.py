num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

def suma(num1, num2):
  var_resultado = num1 + num2
  return var_resultado

resultado = suma(num1, num2)
print("La suma de los dos números es:", resultado)


def resta(num1, num2):
  var_resultado = num1 - num2
  return var_resultado

resultado = resta(num1, num2)
print("La resta de los dos números es:", resultado)


def multiplicacion(num1, num2):
  var_resultado = num1 * num2
  return var_resultado

resultado = multiplicacion(num1, num2)
print("La multiplicacion de los dos números es:", resultado)


def division(num1, num2):
  var_resultado = num1 / num2
  return var_resultado

resultado = division(num1, num2)
print("La division de los dos números es:", resultado)


def modulo(num1, num2):
  var_resultado = num1 % num2
  return var_resultado

resultado = modulo(num1, num2)
print("elresto de los dos números es:", resultado)


def potencia(num1, num2):
  var_resultado = num1 ** num2
  return var_resultado

resultado = potencia(num1, num2)
print("la potencia de los dos números es:", resultado)