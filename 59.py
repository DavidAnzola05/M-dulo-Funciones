def costo_total_DAAC(precio_DAAC, cantidad_DAAC, iva_DAAC):
    subtotal = precio_DAAC * cantidad_DAAC
    return subtotal + (subtotal * iva_DAAC / 100)

print(costo_total_DAAC(50, 3, 19))
