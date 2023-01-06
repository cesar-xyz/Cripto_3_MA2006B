# Se rescrubio el codigo de Descomposicion.py

# Si el MCD(a,b) = 1 si y solo si existen enteros m,n tales que
# 1 = ma +nb, haz un script en julia para encontrar m y n

function MCD(a, b)
    while b != 0
        a, b = b, mod(a, b)
    end
    return a
end

function encontrar_mn(a, b)
    if MCD(a, b) != 1
        return nothing, nothing
    else
        x, y = Euclides(a, b)
        return x, y
    end
end

function Euclides(a, b)
    if b == 0
        return 1, 0
    else
        x, y = Euclides(b, mod(a, b))
        return y, x - y * div(a, b)
    end
end

a = [2, 2, 2]
b = [3, 7, 0]
for i in range(1, length(a))
    m, n = encontrar_mn(a[i], b[i])
    println("m = $m, n = $n")
    println("1 = $(a[i]) * $m + $(b[i]) * $n\n")
end
