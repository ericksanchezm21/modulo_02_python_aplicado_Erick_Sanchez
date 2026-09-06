# Ejercicio 1

producto = "samsung galaxy s28"
precio = 110000.00
en_oferta = True
cantidad_stock = 20

print(producto)
print(precio)
print(en_oferta)
print(cantidad_stock)

print(type(producto), type(precio), type(en_oferta), type(cantidad_stock))

# --------------------------------------------------------------------------------------------------

# Ejercicio 2

total_compra = 18.75
monto_dado = 20

vuelto = monto_dado - total_compra

print("El vuelto dado es de",vuelto)

# --------------------------------------------------------------------------------------------------

# Ejercicio 3

retiro = 37

total_papeletas_10 = retiro // 10
dolares_sobrantes = retiro % 10

print(f"El cajero termino dando {total_papeletas_10} papeletas de 10 dolares y un sobrante de {dolares_sobrantes} dolares.")

# --------------------------------------------------------------------------------------------------

# Ejercicio 4

num1 = float(input("Digite el 1er numero: "))
num2 = float(input("Digite el 2do numero: "))

suma = num1 + num2

print(f"La suma de {num1} y {num2} es igual a {suma}")

# --------------------------------------------------------------------------------------------------

# Ejercicio 5

nota = 95

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"

print (f"{nota}: {letra}")

# --------------------------------------------------------------------------------------------------

# Ejercicio inetgrador

total_compra = float(input("Cual es el monto total de su compra? "))
descuento = 0

if total_compra >= 200:
    descuento = 0.15
elif total_compra >= 100:
    descuento = 0.10

compra_descontada = total_compra*(1-descuento)

print(f"El monto total de su compra sin descuento es de {total_compra}. Como cumple con las condiciones para que se le aplique un {descuento*100}% de descuento, su compra con descuento equivale a {compra_descontada}.")

# --------------------------------------------------------------------------------------------------

# Desafio final

monto_cuenta = float(input("Cual es el monto total de la cuenta? "))
total_personas = int(input("Cuantas personas son en total? "))

if monto_cuenta < 20:
    porc_propina = 0.1
elif monto_cuenta <= 50:
    porc_propina = 0.15
else:
    porc_propina = 0.2

if total_personas > 4:
    porc_propina = porc_propina + 0.05

monto_propina = monto_cuenta*(porc_propina)

monto_con_propina = monto_cuenta + monto_propina
monto_por_persona = monto_con_propina / total_personas

print(f"Como hay que dar de propina un total de {monto_propina}, el monto total a pagar incluyendo la propina es de {monto_con_propina}. Cada uno debera de pagar {monto_por_persona}.")