menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))




dolares = input('¿Cuántos dolares tienes?:  ')
dolares = float(dolares)

valor_yen = 104.473

yenes = str(round( dolares * valor_yen, 2))
#python no es debilmente tipado, solo se pueden combinar los mismo tipos de datos en el print
print('Tienes $' + yenes + ' yenes japoneses en tu cuenta') 