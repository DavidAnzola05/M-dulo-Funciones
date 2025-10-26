def promedio_ponderado_DAAC(notas_DAAC, pesos_DAAC):
    return sum(n * p for n, p in zip(notas_DAAC, pesos_DAAC)) / sum(pesos_DAAC)

print(promedio_ponderado_DAAC([4.0, 3.5, 5.0], [0.3, 0.3, 0.4]))
