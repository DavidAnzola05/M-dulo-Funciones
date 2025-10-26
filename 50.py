def distancia_DAAC(x1_DAAC, y1_DAAC, x2_DAAC, y2_DAAC):
    return ((x2_DAAC - x1_DAAC) ** 2 + (y2_DAAC - y1_DAAC) ** 2) ** 0.5

print(distancia_DAAC(2, 3, 7, 9))
