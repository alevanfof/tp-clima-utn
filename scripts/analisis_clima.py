import pandas as pd
import matplotlib.pyplot as plt

# Inicializamos listas vacías para almacenar temperaturas y precipitaciones
temperaturas = []
precipitaciones = []
# Lista para guardar pares [mes, temperatura] que usaremos después para el gráfico
lista_clima = []

# Inicializamos acumuladores para suma de temperaturas y precipitaciones
temp = 0
lluvia = 0

# Primera apertura del archivo: para cálculos estadísticos
with open("datos/clima_rosario_2025.csv", "r") as archivo:
    lineas = archivo.readlines()  # Leemos todas las líneas del archivo

    # Recorremos desde la línea 1 (saltamos el encabezado)
    for linea in lineas[1:]:
        datos = linea.strip().split(",")  # Separamos por coma y eliminamos espacios/ saltos de línea

        # La temperatura está en la segunda columna (índice 1)
        temperatura = float(datos[1])
        temperaturas.append(temperatura)  # Agregamos a la lista

        # Las precipitaciones están en la tercera columna (índice 2)
        lluvias = float(datos[2])
        precipitaciones.append(lluvias)  # Agregamos a la lista

    # Inicializamos mayor y menor con el primer valor de temperaturas
    mayor = temperaturas[0]
    menor = temperaturas[0]

    # Sumamos todas las temperaturas y buscamos máximos y mínimos
    for i in temperaturas:
        temp = temp + i  # Acumulador para promedio

        if i > mayor:
            mayor = i  # Actualizamos máximo
        if i < menor:
            menor = i  # Actualizamos mínimo

    # Sumamos todas las precipitaciones
    for i in precipitaciones:
        lluvia = lluvia + i  # Acumulador para promedio

# Calculamos temperatura promedio anual (dividimos por 12 meses)
temp_promedio = temp / 12
print(f"La temperatura promedio anual de 2025: {temp_promedio:.2f} °C")
print("Temperatura máxima:", mayor)
print("Temperatura minima", menor)

# Calculamos precipitación promedio anual
lluvia_promedio = lluvia / 12
print(f"Las precipitaciones promedio anual de 2025: {lluvia_promedio:.2f} mm")

# Segunda apertura del archivo: para preparar datos del gráfico
with open("datos/clima_rosario_2025.csv", "r") as archivo:
    lineas = archivo.readlines()  # Leemos nuevamente el archivo

    # Recorremos desde la línea 1 (saltamos el encabezado)
    for linea in lineas[1:]:
        datos = linea.strip().split(",")  # Separamos por coma

        # El mes está en la primera columna (índice 0)
        mes = datos[0]
        # La temperatura está en la segunda columna (índice 1)
        temperatura = float(datos[1])

        # Guardamos el par [mes, temperatura] para el gráfico
        lista_clima.append([mes, temperatura])

# Convertimos la lista a DataFrame de pandas para graficar más fácil
datos = pd.DataFrame(lista_clima, columns=["Mes", "Temperatura"])
# Generamos gráfico de barras con matplotlib (pandas usa matplotlib detrás)
datos.plot.bar(x="Mes", y="Temperatura")
# Guardamos el gráfico como imagen en la carpeta /resultados
plt.savefig("resultados/grafico_temperaturas.png")
