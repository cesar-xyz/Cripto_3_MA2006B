def calculate_elements(n, a, b):
    # Check if the curve is valid
    if (4 * (a ** 3) + 27 * (b ** 2)) % n == 0:
        return "Invalid curve"
    else:
        # Choose a point P on the curve
        for x in range(n):
            eval = (6 ** 3 + 6 * 2 + 2) % n
            print(eval,x**2)
            if (eval == x**2):
                print(x)


# Example usage

def main():
    n = 17
    a = 6
    b = 3
    calculate_elements(n, a, b)


if __name__ == '__main__':
    main()
