def promedio_calificaciones_DAAC(notas_DAAC):
    return round(sum(notas_DAAC) / len(notas_DAAC), 2)

print(promedio_calificaciones_DAAC([3.5, 4.0, 5.0, 4.2]))
