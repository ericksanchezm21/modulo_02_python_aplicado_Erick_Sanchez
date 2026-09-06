#  Ejercicio 1

horas_estudio = [2, 3, 1, 4, 2, 5, 3]

total_horas_estudiadas = 0
total_dias = 0
total_dias_mayores_iguales_3 = 0

for hora in horas_estudio:
    if hora >= 3:
        total_dias_mayores_iguales_3 += 1
    total_horas_estudiadas += hora
    total_dias += 1

promedio_diario = total_horas_estudiadas / total_dias

print(f"Total de horas estudiadas: {total_horas_estudiadas}")
print(f"Horas diarias promedio de estudio: {round(promedio_diario, 1)}")
print(f"Total de dias en las que se estudio mas de 3 horas: {total_dias_mayores_iguales_3}")

# ---------------------------------------------------------------------------------------------------

# Ejercicio 2

ahorro = 0
cantidad_ahorrar_semana = 45
cantidad_semanas = 0

while ahorro < 300:
    ahorro += cantidad_ahorrar_semana
    cantidad_semanas += 1

print(f"Total de ahorro obtenido: {ahorro}.")
print(f"Total de semanas completas dedicadas a ahorrar: {cantidad_semanas}.")

# ---------------------------------------------------------------------------------------------------

# Ejercicio 3

def calcular_costo_envio(peso, distancia):
    return (peso * 0.5) + (distancia * 0.1)

def clasificar_envio(costo):
    if costo < 10:
        return "Economico"
    elif costo < 25:
        return "Estandar"
    else:
        return "Premiun"

peso = 12
distancia = 80

costo = calcular_costo_envio(peso, distancia)
clasificacion_envio = clasificar_envio(costo)

print(f"El costo de enviar un paquete de {peso} kg por una distancia de {distancia} km es de ${round(costo,2)}, lo cual lo califica como un envio {clasificacion_envio}")

# ---------------------------------------------------------------------------------------------------

# Ejercicio 4

peliculas = ["Coco", "Interestelar", "Matrix", "Toy Story", "Origen", "Encanto"]

print("Listado total de peliculas:", peliculas)
print("Primera pelicula del listado:", peliculas[0])
print("Ultima pelicula del listado:", peliculas[-1])
print("Las 3 primeras peliculas del listado:", peliculas[:3])
print("Total de peliculas en el listado:", len(peliculas))
print("Peliculas en las posiciones (0,2,4):", peliculas[::2])
print("Peliculas entre la posiciones 1 y 3:", peliculas[1:4])

# ---------------------------------------------------------------------------------------------------

# Ejercicio 5

carrito = ["pantalon", "camisa"]

carrito.append("zapatos")
print(carrito)
carrito.insert(0, "cinturon")
print(carrito)
carrito.remove("pantalon")
print(carrito)
print("camisa esta en carrito", "camisa" in carrito)
carrito.sort()
print(carrito)

# ---------------------------------------------------------------------------------------------------

# Ejercicio 6

asientos = [
["L", "X", "L"],
["X", "X", "L"],
["L", "L", "X"],
]

print("Primera fila:", asientos[0])
print("Asiento 1ra fila 2da columna:", asientos[0][1])

print("Filas existentes:")
for fila in asientos:
    print(fila)

ventas_vendedores = [
["Marta", 320, 450, 275],
["Julio", 180, 200, 210],
]

for vendedor in ventas_vendedores:
    nombre_vendedor = vendedor[0]
    total_ventas_vendedor = sum(vendedor[1:])
    print(f"{nombre_vendedor}: {total_ventas_vendedor}")

# ---------------------------------------------------------------------------------------------------

# Ejercicio 7

color = (120, 200, 50)

print(color)
print(color[0], color[1], color[2])
print(type(color))

def calcular_brillo(c):
    return sum(c)/len(c)

color_a = (120, 200, 50) 
color_b = (10, 10, 10)

brillo_a = calcular_brillo(color_a)
brillo_b = calcular_brillo(color_b)

print("Brillo color a:", brillo_a)
print("Brillo color b:", brillo_b)

if brillo_a > brillo_b:
    print("El color a es mas brillante que el color b")
else:
    print("El color b es mas brillante que el color a")

# ---------------------------------------------------------------------------------------------------

# Desafio final

def clasificar_equipo(total):
    if total >= 60:
        return "Campeon"
    elif total >= 40:
        return "Finalista"
    else:
        return "Participante"

equipos = [
["Halcones", 12, 14, 10],
["Titanes", 30, 28, 15],
["Fenix", 18, 16, 20],
]

puntuacion_maxima = 0

print("---Equipos participantes---")
for equipo in equipos:
    nombre_equipo = equipo[0]
    puntuacion_equipo = sum(equipo[1:])
    clasificacion_equipo = clasificar_equipo(puntuacion_equipo)
    if puntuacion_equipo > puntuacion_maxima:
        puntuacion_maxima = puntuacion_equipo
        equipo_ganador = equipo
    print(f"Equipo: {nombre_equipo}. Puntuacion: {puntuacion_equipo}. Clasificacion: {clasificacion_equipo}.")

print("---------------------------------")
print("Equipo ganador:", equipo_ganador[0])

puntuacion_equipo_ganador = sum(equipo_ganador[1:])

total_rondas_bonus = 0
puntuacion_ronda_bonus = 5

while puntuacion_equipo_ganador < 70:
    puntuacion_equipo_ganador += puntuacion_ronda_bonus
    total_rondas_bonus += 1

print("---------------------------------")
print("Rondas bonus para el equipo", equipo_ganador[0])
print("--Total de rondas:", total_rondas_bonus)
print("--Puntuacion total final", puntuacion_equipo_ganador)

print("---------------------------------")
print("Resultado final del equipo ganador")
equipo_ganador_tupla = (equipo_ganador[0], clasificar_equipo(puntuacion_equipo_ganador))
print(equipo_ganador_tupla)




