__author__ = 'solomina'

total_value = 4
def factory_power(pow_value):
    """
    Factory for generate power_functions
    """

    def square(n):
        return "%s(%i) = %i" % (square.func_name, n, n * n)

    def cybe(n):
        return "%s(%i) = %i" % (cube.func_name, n, n*n*n)

    if pow_value == 2:
        return square
    elif pow_value == 3:
        return cybe
    else:
        return None

square = factory_power(2)
print square(total_value)
cube = factory_power(3)
print cube(total_value + 10)


