
def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])

    poblacion = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424,
    }

    # print(poblacion['Argentina'])

    # for pais in poblacion.keys():
    #     print(pais)

    # for pais in poblacion.values():
    #     print(pais)
    
    for pais, numero in poblacion.items():
        print( pais + ' tiene una población de ' + str(numero) + ' de personas')



if __name__ == '__main__':
    run()