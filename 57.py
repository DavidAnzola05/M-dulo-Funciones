def promedio_aprobadas_DAAC(notas_DAAC):
    aprobadas = [n for n in notas_DAAC if n >= 3]
    return sum(aprobadas) / len(aprobadas) if aprobadas else 0

print(promedio_aprobadas_DAAC([2.5, 3.8, 4.0, 2.9, 5.0]))
