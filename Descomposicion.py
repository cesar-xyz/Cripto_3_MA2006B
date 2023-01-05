# Si el MCD(a,b) = 1 si y solo si existen enteros m,n tales que
# 1 = ma +nb, haz un script en python para encontrar m y n

def Euclides(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = Euclides(b, a % b)
        return y, x - y * (a // b)


a = [2, 2]
b = [3, 7]
for i in range(0, len(a)):
    m, n = Euclides(a[i], b[i])
    print(f"m = {m}, n = {n}")

a = 23
b = 6
m, n = Euclides(a, b)
print(f"m = {m}, n = {n}")
