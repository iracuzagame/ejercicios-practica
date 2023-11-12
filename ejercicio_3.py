#Construye un programa que al recibir como dato el radio de un circulo, calcule e imprima tanto su área como la longitud de su circunferencia.
#El área de un circulo la calculamos como: Area=n*radio^2
#La circunferencia del circulo la calculamos de la siguiente forma: longitud de la circunferencia= 2*n*radio

import math

rad=float(input("Ingrese el radio del circulo: "))
area=math.pi*pow(rad,2)
longitud=2*math.pi*rad

print("El area del circulo es: ",area)
print("La longitud del circulo es: ", longitud)
