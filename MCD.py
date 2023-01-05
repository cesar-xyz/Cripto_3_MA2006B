# Algoritmo de MCD
'''
Con recursividad

def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b  # Resto de la división
        return mcd(b, r)
'''


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Ejemplo de uso
print(mcd(8, 4))  # Salida: 4
