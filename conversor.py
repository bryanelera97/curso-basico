soles = input("¿cuantos soles quieres cambiar?: ")
soles = float(soles)
valor_dolar = 3.50
dolares = soles/valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("tienes $" + dolares + " " + "dólares")