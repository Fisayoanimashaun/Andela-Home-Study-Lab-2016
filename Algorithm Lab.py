def binary_converter(x):
    if (isinstance(x, int)) and (x in range(0, 256)):
        return (bin(x)[2:])
    else:
        return "Invalid input"

print binary_converter(0)
print binary_converter(62)
print binary_converter(-1)
print binary_converter(300)
