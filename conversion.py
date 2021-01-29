#python no es debilmente tipado, solo se pueden combinar los mismo tipos de datos en el print

menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

def conversion(tasa, pais):
    pesos = input('¿Cuántos pesos ' + pais + ' tienes?:  ')
    pesos = float(pesos)
    valor_dolar = tasa
    dolar = str(round( pesos / valor_dolar, 2))
    print('Tienes $' + dolar + ' dolares en tu cuenta')

if opcion == 1:
    conversion(3875, 'colombianos')
elif opcion == 2:
    conversion(65, 'argentinos')
elif opcion == 3:
    conversion(24, 'mexicanos')
else:
    print('Ingrese una respuesta válida')