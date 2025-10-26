def tipo_numero_DAAC(n_DAAC):
    if n_DAAC > 0:
        return "Positivo"
    elif n_DAAC < 0:
        return "Negativo"
    else:
        return "Cero"

print(tipo_numero_DAAC(-7))
