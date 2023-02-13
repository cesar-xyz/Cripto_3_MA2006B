function Euclides(m, n)
    r = 0
    while r < n
        for q in 0:m
            if m == q * n + r
                println("$m = $q * $n + $r")
                break
            end
        end
        r += 1
    end
end

# Ejemplo de uso

Euclides(12, 8)
Euclides(60, 48)
Euclides(11, 2)
Euclides(25, 2)
Euclides(7, 2)
