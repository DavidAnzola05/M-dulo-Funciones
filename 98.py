def segundos_a_tiempo_DAAC(segundos_DAAC):
    dias = segundos_DAAC // 86400
    segundos_DAAC %= 86400
    horas = segundos_DAAC // 3600
    segundos_DAAC %= 3600
    minutos = segundos_DAAC // 60
    return dias, horas, minutos

print(segundos_a_tiempo_DAAC(200000))
