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


def euler(n):
    a = len(calcularU(n))
    return a


def inversos(G, n):
    for i in G:
        for j in G:
            if (i * j) % n == 1:
                print('(', i, '*', j, f") % {n}  = {(i * j) % n}")


def asociatividad(S):
    for a in S:
        for b in S:
            for c in S:
                if ((a * b) * c) % 8 != (a * (b * c)) % 8:
                    return "No tiene asociatividad"
                print(a,b,c)
    return "Si tiene asociatividad"


def main():
    # 1.- Programar la función de Euler:
    # Es decir, si es un número natural mayor que 1 escribir una
    # función que calcule el número de primos relativos a n  y menores a n.

    print("ƒ(n)-", euler(9))

    # 2.-Verificar que U_8 es un grupo bajo la multiplicación.
    # Verificar si tiene neutro
    # Todos sus elementos tienen inverso
    # Por transitividad
    n = 8
    U = calcularU(n)
    print(U)
    # Si tiene todos sus elementos inverso.
    inversos(U, n)
    print(asociatividad(U))

    #

if __name__ == '__main__':
    main()
