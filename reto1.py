import random

def run():
    numero = random.random()
    numero = numero * 100

    for i in range(1,101):
        if i > numero:
            break

        if i % 2 != 0:
            continue
        print(i)
        
    print(numero)


if __name__ == '__main__':
    run()
