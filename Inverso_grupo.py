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
    listInv= []
    for a in U:
        fi = phi(n)
        listInv.append(pow(a, fi - 1) % n)
    return listInv

def inversos_fermat(G, p):
    for a in G:
        print(pow(a, p - 2) % p)


def asociatividad(S, n, u=False):
    for a in (S):
        for b in S:
            for c in S:
                if ((a * b) * c) % n != (a * (b * c)) % n:
                    return "No tiene asociatividad"
    return f"El grupo {'U' if u else 'Z'}, n = {n}.\nSi tiene asociatividad.\n"

def inversos(U,n):
    if len(inverso_euler(U, n)) == len(U):
        print("Todos los elementos del grupo tienen inversos.")
    else:
        print("No todos los elementos del grupo tienen inversos.")

def main():
    '''

    n = 131
    U = list(range(50, 61))
    inversos_fermat(U, n)
    inverso_euler(U, n)

    U = calcularU(12)
    inversos_fermat(U, 12)
    inverso_euler(U, 12)

    inversos_fermat([127], 45775)
    inverso_euler([127], 45775)
    '''
    #1) U_125
    n = 125
    print('-',n)
    U = calcularU(n)
    inversos(U,n)
    print(asociatividad(U, n, True))

    #2) U_1023
    n = 1023
    print('-',n)
    U = calcularU(n)
    inversos(U,n)
    print(asociatividad(U, n, True))

    #3) Z_203
    n = 203
    print('-',n)
    Z = list(range(1,n))
    inversos(U,n)
    print(asociatividad(U, n))

    #4) Z_1021
    n = 1021
    print('-',n)
    Z = list(range(1, n + 1))
    inversos(U,n)
    print(asociatividad(U, n))

if __name__ == '__main__':
    main()
