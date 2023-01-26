def exp(a, n):
    init_a = a
    for bi in bin(n)[3::]:
        if bi == '0':
            a = a ** 2
        else:
            a = (a ** 2) * init_a
    return a


def main():
    print(exp(2, 79) % 101)


if __name__ == '__main__':
    main()
