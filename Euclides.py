# Euclides
# m = q*n + r
# si 0≤r<n
'''
def Euclides(m,n):
    q = m // n
    r = m % n
    return [q,r]
    
def Euclides(m,n):
    for r in range(0, m):
        for q in range(0,m):
            if(r<n and m == q*n+r):
                print(m,'=',q,'*',n,'+',r)
'''


def Euclides(m, n):
    r = 0
    while r < n:
        for q in range(0, m):
            if m == q * n + r:
                print(m, '=', q, '*', n, '+', r)
                break
        r += 1


# Ejemplo de uso

Euclides(12, 8)
Euclides(60, 48)
Euclides(11, 2)
Euclides(25, 2)
Euclides(7, 2)
