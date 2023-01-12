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
        a = b
        b = a % b
    return a


# Ejemplo de uso
def main():
    print(mcd(4, 6))  # Salida: 4

if __name__ == '__main__':
    main()