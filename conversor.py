menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 💵💵💵💵

1 - PESOS COLOMBIANOS
2 - SOLES PERUANOS
3 - PESOS MEXICANO

ELIGE UNA OPCIÓN:  """ 

opcion = int(input(menu))

if opcion == 1:
    soles = input("¿cuantos pesos colombianos quieres cambiar?: ")
    soles = float(soles)
    valor_dolar = 3875
    dolares = soles/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " " + "dólares")
elif opcion ==2:
    soles = input("¿cuantos soles quieres cambiar?: ")
    soles = float(soles)
    valor_dolar = 3.50
    dolares = soles/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " " + "dólares")
elif opcion ==3:
    soles = input("¿cuantos pesos mexicanos quieres cambiar?: ")
    soles = float(soles)
    valor_dolar = 24
    dolares = soles/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " " + "dólares")
else:
    print('ingresa una opción correcta por favor')


