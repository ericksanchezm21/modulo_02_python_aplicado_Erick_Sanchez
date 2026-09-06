import numpy as np

# Ejercicio 1

calificaciones = np.array([88, 92, 76, 95, 81, 68])

print("Primera nota:", calificaciones[0])
print("Ultima nota:", calificaciones[-1])
print("Notas desde la posicion 2 hasta la 4:", calificaciones[2:5])
print("Cantidad total de notas", len(calificaciones))

# -------------------------------------------------------------------------------------------------

# Ejercicio 2

comisiones = np.array([120.50, 340.00, 89.75, 210.25])

print("Comisiones con un bono del 10%:", np.round(comisiones*1.1,2))

# -------------------------------------------------------------------------------------------------

# Ejercicio 3

consumo_gb = np.array([2.3, 5.1, 1.8, 8.4, 3.6, 4.2, 6.9])

print("Consumo promedio diario:", round(np.mean(consumo_gb),2))
print("Consumo maximo diario:", round(np.max(consumo_gb),2))
print("Consumo minimo diario:", round(np.min(consumo_gb),2))
print("Desviacion estandar:", round(np.std(consumo_gb),2))

# -------------------------------------------------------------------------------------------------

# Ejercicio 4

horas_estudio = np.array([
[5, 8, 6, 7],
[10, 9, 11, 8],
[3, 4, 2, 5],
])

print("Calculo del promedio de horas estudiadas por estudiante:", np.round(np.mean(horas_estudio, axis = 1),2))
print("Calculo del promedio de horas estudiadas por semana:", np.round(np.mean(horas_estudio, axis = 0),2))

# -------------------------------------------------------------------------------------------------

# Desafio final

ventas = np.array([
[1200, 1350, 980, 1420, 1100],
[850, 920, 1050, 890, 960],
[1600, 1750, 1580, 1690, 1720],
])

print("Total de ventas por sucursal:", np.sum(ventas, axis = 1))
print("Comision del 5 por ciento sobre las ventas por sucursal:", np.round(np.sum(ventas, axis = 1) * 0.05, 2))
print("Total de ventas por por dia:", np.sum(ventas, axis = 0))

variacion_por_sucursal = np.round(np.std(ventas, axis = 1), 2)

minima_variacion = np.min(variacion_por_sucursal)

for i in range(len(variacion_por_sucursal)):
    print(f"Variacion en ventas de la Sucursal no. {i+1}: {variacion_por_sucursal[i]}")
    if variacion_por_sucursal[i] == minima_variacion:
        sucursal_menor_variacion = f"Sucursal no. {i+1}"

print("Sucursal con las ventas diarias mas consistentes:", sucursal_menor_variacion)

