def run():
    LIMITE = 1000 

    contador = 0
    potencia = 0

    while potencia < LIMITE:
        potencia = 2**contador
        print('2 elevado a la potencia ' + str(contador) + ' es = ' + str(potencia))
        contador = contador + 1
        

if __name__ == '__main__':
    run()