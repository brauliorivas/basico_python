def es_primo(numero):

    if numero == 1 or numero % 2 == 0:
        return False

    if numero == 2:
        return True

    veces = 1

    for i in range(3, numero + 1):
        if numero % i == 0:
            veces += 1

    if veces > 2:
        return False
    else:
        return True   

def run():
    numero = int(input('Ingrese un numero: '))
    if es_primo(numero):
        print('Es un número primo')
    else:
        print('No es numero primo')

if __name__ == '__main__':
    run()