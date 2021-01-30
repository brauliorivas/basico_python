if __name__ == '__main__':
    palabra = input('Ingresa una palabra: ')
    palabra = palabra.replace(' ', '').lower()
    invertida = palabra[::-1]
    def palindrome():
        if invertida == palabra:
            print('Es palindroma')
        else:
            print('No es palidrome')
    palindrome()
