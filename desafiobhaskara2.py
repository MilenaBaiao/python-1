import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

raíz1 = (-b + math.sqrt(delta)) / (2*a)
raíz2 = (-b - math.sqrt(delta)) / (2*a)

if delta == 0:
    raíz1 = (-b + math.sqrt(delta)) / (2*a)
    print("A única raíz é: ", raíz1)
else:
  if delta < 0:
      print("Essa equação não possui raízes reais")
  else:
      raíz1 = (-b + math.sqrt(delta)) / (2*a)
      raíz2 = (-b - math.sqrt(delta)) / (2*a)
      print("A primeira raíz é: ", raíz1)
      print("A segunda raíz é: ", raíz2)
      
      
