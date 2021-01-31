import random

def adivina():
    numero =  random.randint(1, 100)
    return numero


def run():
    ingresa = int(input('Adivina un número del 1 al 100: '))

    num = adivina()
    
    while ingresa != num:
        if ingresa > num:
            ingresa = int(input('Ingresa un número menor: '))
        else:
            ingresa = int(input('Ingresa un número mayor: '))

    print('Ganaste, el número era el: ' + str(num))


if __name__ == '__main__':
    run()