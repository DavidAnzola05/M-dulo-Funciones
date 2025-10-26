def media_geometrica_DAAC(lista_DAAC):
    producto = 1
    for n in lista_DAAC:
        producto *= n
    return producto ** (1 / len(lista_DAAC))

print(media_geometrica_DAAC([2, 8]))
