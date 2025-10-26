def potencia_manual_DAAC(base_DAAC, exponente_DAAC):
    resultado_DAAC = 1
    for _ in range(exponente_DAAC):
        resultado_DAAC *= base_DAAC
    return resultado_DAAC

print(potencia_manual_DAAC(2, 5))
