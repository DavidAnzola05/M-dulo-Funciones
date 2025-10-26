def minutos_a_horas_DAAC(minutos_DAAC):
    horas = minutos_DAAC // 60
    mins = minutos_DAAC % 60
    return horas, mins

print(minutos_a_horas_DAAC(135))
