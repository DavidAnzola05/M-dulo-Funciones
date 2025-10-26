def precio_final_DAAC(precio_DAAC, descuento_DAAC, iva_DAAC):
    precio_con_descuento = precio_DAAC - (precio_DAAC * descuento_DAAC / 100)
    return precio_con_descuento + (precio_con_descuento * iva_DAAC / 100)

print(precio_final_DAAC(1000, 10, 19))
