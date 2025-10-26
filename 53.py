def es_bisiesto_DAAC(anio_DAAC):
    return (anio_DAAC % 4 == 0 and anio_DAAC % 100 != 0) or (anio_DAAC % 400 == 0)

print(es_bisiesto_DAAC(2024))
