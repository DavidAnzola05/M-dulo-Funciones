def suma_digitos_DAAC(numero_DAAC):
    return sum(int(d) for d in str(abs(numero_DAAC)))

print(suma_digitos_DAAC(4567))
