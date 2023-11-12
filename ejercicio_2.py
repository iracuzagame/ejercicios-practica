# Construye un programa que, al recibir como datos el costo de un articulo vendido y la capital de dinero entregado por el cliente, calcular en prima.

#1. El cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del producto.
#2. ¿Qué pasa si el cliente paga exactamente lo que vale el producto?
#3. La cantidad de dinero que falta por pagar si el pago efectuado es menor que el precio del producto.

preventa = float(input("Ingrese el precio del producto: "))
pago = float(input("Ingrese el monto cancelado por el cliente: "))
cambio = pago-preventa
faltante = preventa-pago

if (cambio<0):
    print("EL dinero faltante es de: ", faltante)

if (cambio>0):
    print("El a dar es de ", cambio)
    
elif (cambio==0):
    print("Se ha pagado en su totalidad")
