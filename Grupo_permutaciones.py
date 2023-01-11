def permutation(list):
    if len(list) == 0:
        return [[]]
    else:
        return [[x] + ys for x in list for ys in permutation(delete(list, x))]


def delete(list, item):
    lc = list[:]
    lc.remove(item)
    return lc


def operacion(list, Oplist):
    a = []
    for i in list:
        a.append(Oplist[i - 1])
    return a


def subgrupos(list, identidad):
    sub = 1
    for i in list:
        if operacion(i, i) == identidad and i != identidad:
            print('f', sub, '->', i)
        sub += 1


def main():
    S = [1, 2, 3]
    subgrupos(permutation(S), S)

    # Operacion de 3 elementos
    a = operacion([2, 3, 1], S)
    print(operacion([3, 1, 2], a))


if __name__ == '__main__':
    main()
