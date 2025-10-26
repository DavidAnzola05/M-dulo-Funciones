def contar_pares_DAAC(lista_DAAC):
    return len([n for n in lista_DAAC if n % 2 == 0])

print(contar_pares_DAAC([2, 5, 6, 9, 10]))
