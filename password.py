import random
import string

def generate_password():
    mayusculas = list(string.ascii_uppercase[:26])
    minusculas = list(string.ascii_lowercase[:26])
    simbolos = ['!', '@', '$', '%', '#']
    
    numeros = []

    for i in range(0,10):
        numeros.append(str(i))

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    #reduce una lista a un string, la lista debe ser del mismo tipo de variable

    return password


def run():
    password = generate_password()
    print('Tu nueva contraseña es ' + password)


if __name__ == '__main__':
    run()
