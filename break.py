def run():
    for contador in range(1, 51):
        if contador % 2 != 0:
            continue
        # por ejemplo, si se cumple, continue hace que termine ahi el codigo y repita
        print(contador)

    for i in range(51):
        if i == 26:
            break
        print(i)
        #si se cumple, para todo el proceso dentro de ese scope

if __name__ == '__main__':
    run()