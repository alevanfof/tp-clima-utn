import pandas as pd
import matplotlib.pyplot as plt

temperaturas = []
precipitaciones = []
lista_clima = []

temp = 0
lluvia = 0

with open("datos/clima_rosario_2025.csv", "r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas[1:]:
        datos = linea.strip().split(",")

        temperatura = float(datos[1])
        temperaturas.append(temperatura)

        lluvias = float(datos[2])
        precipitaciones.append(lluvias)


    mayor = temperaturas[0]
    menor = temperaturas[0]

    for i in temperaturas:

        temp = temp + i

        if i > mayor:
            mayor = i

        if i < menor:
            menor = i


    for i in precipitaciones:

        lluvia = lluvia + i


temp_promedio = temp / 12
print(f"La temperatura promedio anual de 2025: {temp_promedio:.2f} °C")
print("Temperatura máxima:", mayor)
print("Temperatura minima", menor)
lluvia_promedio = lluvia / 12
print(f"Las precipitaciones promedio anual de 2025: {lluvia_promedio:.2f} mm")

with open("datos/clima_rosario_2025.csv", "r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas[1:]:
        datos = linea.strip().split(",")

        mes = datos[0]
        temperatura = float(datos[1])

        lista_clima.append([mes, temperatura])

#print(lista_clima)

datos = pd.DataFrame(lista_clima, columns=["Mes", "Temperatura"])
datos.plot.bar(x="Mes", y="Temperatura")
plt.savefig("resultados/grafico_temperaturas.png")