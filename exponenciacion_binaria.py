def exp(a, n):
    for bi in bin(n)[3::]:
        if bi == '0':
            a = a ** 2
        else:
            a = (a ** 2) * 2
    return a


def main():
    print(exp(24, 600000) % 94358430989)


if __name__ == '__main__':
    main()
