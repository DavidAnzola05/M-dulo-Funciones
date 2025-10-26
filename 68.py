def es_primo_DAAC(n_DAAC):
    if n_DAAC < 2:
        return False
    for i in range(2, int(n_DAAC ** 0.5) + 1):
        if n_DAAC % i == 0:
            return False
    return True

print(es_primo_DAAC(29))
