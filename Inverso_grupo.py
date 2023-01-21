def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b  # Resto de la división
        return mcd(b, r)


def calcularU(n):
    a = []
    for i in range(1, n + 1):
        if mcd(i, n) == 1:
            a.append(i)
    return a


def phi(n):
    a = len(calcularU(n))
    return a


def inverso_euler(U, n):
    listInv = []
    for a in U:
        fi = phi(n)
        listInv.append(pow(a, fi - 1) % n)
    return listInv


def inverso_fermat(G, p):
    listInv = []
    for a in G:
        listInv.append(pow(a, p - 1) % p)
    return listInv


def asociatividad(S, n, u=False):
    for a in S:
        for b in S:
            for c in S:
                if ((a * b) * c) % n != (a * (b * c)) % n:
                    return "No tiene asociatividad"
    return f"El grupo {'U' if u else 'Z'}, n = {n}.\nSi tiene asociatividad.\n"


def inversos(U, n):
    if len(inverso_euler(U, n)) == len(U):
        print("Todos los elementos del grupo tienen inversos.")
    else:
        print("No todos los elementos del grupo tienen inversos.")


def main():
    n = 640
    print('-', n)
    U = calcularU(n)
    print(inverso_fermat([49], n))
    print(inverso_euler([49], n))
    print(asociatividad(U, n, True))
    '''
    """ 1.- Verificar que los siguientes conjuntos con la operación de multiplicación (módulo n) son grupos o no."""
    # 1) U_125
    n = 125
    print('-', n)
    U = calcularU(n)
    inversos(inverso_euler(U, n), n)
    print(asociatividad(U, n, True))

    # 2) U_1023
    n = 1023
    print('-', n)
    U = calcularU(n)
    inversos(inverso_euler(U, n), n)
    print(asociatividad(U, n, True))

    # 3) Z_203
    n = 203
    print('-', n)
    Z = list(range(1, n))
    inversos(inverso_euler(Z, n), n)
    print(asociatividad(Z, n))

    # 4) Z_1021
    n = 1021
    print('-', n)
    Z = list(range(1, n + 1))
    inversos(inverso_euler(Z, n), n)
    print(asociatividad(Z, n))

    """ 2.- Calcular los inversos del grupo U_131 de los elementos:"""
    # a = 50, 51, 52, ..., 60
    n = 131
    print('-', n,"\na = [50,51...,60]")
    U = list(range(50, 61))
    print("Fermat:")
    print(inverso_fermat(U, n))
    print("Euler:")
    print(inverso_euler(U, n))
'''

if __name__ == '__main__':
    main()
