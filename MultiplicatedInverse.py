def has_modular_inverse(array):
    for a in array:
        for b in array:
            if (a * b) % len(array) == 1:
                print(a, b)


# Test the function
# z = 6
array = [0, 1, 2, 3, 4, 5]

has_modular_inverse(array)
