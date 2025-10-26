def contar_mayusculas_DAAC(texto_DAAC):
    return sum(1 for c in texto_DAAC if c.isupper())

print(contar_mayusculas_DAAC("Hola Mundo Python"))
