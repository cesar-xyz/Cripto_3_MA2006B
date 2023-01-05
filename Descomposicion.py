# Si el MCD(a,b) = 1 si y solo si existen enteros m,n tales que
# 1 = ma +nb, haz un script en python para encontrar m y n

def MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def encontrar_mn(a, b):
    mcd = MCD(a, b)
    if mcd != 1:
        return None, None
    else:
        x, y = Euclides(a, b)
        return x, y


def Euclides(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = Euclides(b, a % b)
        return y, x - y * (a // b)


a = [2, 2, 2]
b = [3, 7, 0]
for i in range(0, len(a)):
    m, n = encontrar_mn(a[i], b[i])
    print(f"m = {m}, n = {n}")
    print(f"1 = {a[i]} * {m} + {b[i]} * {n}\n")
