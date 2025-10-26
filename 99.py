def promedio_armonico_DAAC(lista_DAAC):
    return len(lista_DAAC) / sum(1/x for x in lista_DAAC)

print(promedio_armonico_DAAC([2, 4, 6]))
