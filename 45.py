def contar_vocales_DAAC(palabra_DAAC):
    return sum(1 for letra in palabra_DAAC.lower() if letra in "aeiou")

print(contar_vocales_DAAC("Programacion"))
