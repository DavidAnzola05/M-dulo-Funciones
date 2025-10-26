def calcular_iva_DAAC(precio_DAAC, tasa_DAAC):
    return precio_DAAC * (tasa_DAAC / 100)

print(calcular_iva_DAAC(200, 19))
