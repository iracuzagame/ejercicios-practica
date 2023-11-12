#En una casa de cambio necesitan construir un programa tal que al dar como dato una cantidad expresada en dolares, convierta esa cantidad a euros.

pDolar= float(input("Ingrese el precio actual del dolar a Euro: "))
CantDolar=float(input("Ingrese la cantida de dolares a convertir: "))
cEuro= CantDolar*pDolar

print(CantDolar,"$ Equivale a", cEuro,"EUR")