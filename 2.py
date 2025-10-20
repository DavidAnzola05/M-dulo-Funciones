import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio:.5f} segundos en ejecutarse")
        return resultado
    return envoltura

@medir_tiempo
def calcular_suma_grande():
    return sum(range(1000000))

resultado = calcular_suma_grande()
print(f"La suma calculada es: {resultado}")