def interes_compuesto_DAAC(capital_DAAC, tasa_DAAC, tiempo_DAAC):
    return capital_DAAC * ((1 + tasa_DAAC / 100) ** tiempo_DAAC)

print(interes_compuesto_DAAC(1000, 5, 2))
