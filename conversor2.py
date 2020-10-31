def conversor(tipo_moneda, valor_dolar):
    moneda = input("¿ cuantos"+ " "+ tipo_moneda + " " + "quieres cambiar?: ")
    moneda = float(moneda)
    dolares = moneda/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " " + "dólares")
    
menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 💵💵💵💵

1 - PESOS COLOMBIANOS
2 - SOLES PERUANOS
3 - PESOS MEXICANO

ELIGE UNA OPCIÓN:  """ 

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos Colombianos", 3875)
    
elif opcion ==2:
    conversor("Soles Peruanos", 3.50)
    
elif opcion ==3:
      conversor("Pesos Mexicanos", 3.50)
else:
    print('ingresa una opción correcta por favor')