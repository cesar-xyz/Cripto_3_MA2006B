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
    for a in U:
        fi = phi(n)
        print(a, '->', (pow(a, fi - 1)) % n)


def inversos_fermat(G, p):
    for a in G:
        print(pow(a, p - 2) % p)


def main():
    n = 131
    U = list(range(50, 61))
    inversos_fermat(U, n)
    inverso_euler(U, n)

    U = calcularU(12)
    inversos_fermat(U, 12)
    inverso_euler(U, 12)

    inversos_fermat([127], 45775)
    inverso_euler([127], 45775)

    U = calcularU(125)
    inverso_euler(U, 125)


if __name__ == '__main__':
    main()
