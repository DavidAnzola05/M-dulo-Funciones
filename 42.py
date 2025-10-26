def factorial_DAAC(n_DAAC):
    resultado_DAAC = 1
    for i in range(1, n_DAAC + 1):
        resultado_DAAC *= i
    return resultado_DAAC

print(factorial_DAAC(5))
