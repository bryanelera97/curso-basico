# contador = 0
# print('2 elevado a ' + str(contador) + 'es igual a: ' + str(2**contador))

# contador = 1
# print('2 elevado a ' + str(contador) + 'es igual a: ' + str(2**contador))

# contador = 2
# print('2 elevado a ' + str(contador) + 'es igual a: ' + str(2**contador))

# contador = 3
# print('2 elevado a ' + str(contador) + 'es igual a: ' + str(2**contador))

def run():
    LIMITE = 1000000

    contador = 0
    pontencia_2 = 2**contador
    while pontencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + 'es igual a: ' + str(pontencia_2))
        contador = contador + 1
        pontencia_2 = 2**contador

        

if __name__== '__main__':
    run()