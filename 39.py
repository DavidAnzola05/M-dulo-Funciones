def salario_total_DAAC(horas_DAAC, tarifa_DAAC):
    if horas_DAAC <= 40:
        return horas_DAAC * tarifa_DAAC
    else:
        extra = horas_DAAC - 40
        return (40 * tarifa_DAAC) + (extra * tarifa_DAAC * 1.5)

print(salario_total_DAAC(45, 20000))
