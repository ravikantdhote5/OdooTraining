
#Type Conversion
def convert(data):
    if isinstance(data, tuple):
        # Convert tuple to list
        return list(data)

    elif isinstance(data, list):
        # Convert list to set
        return set(data)

    elif isinstance(data, set):
        # Convert set to tuple
        return tuple(data)

    else:
        return "Unsupported type"

print(convert((1, 2, 3)))   # Output: [1, 2, 3]
print(convert([1, 2, 2, 3])) # Output: {1, 2, 3}
print(convert({1, 2, 3}))   # Output: (1, 2, 3)
print(convert("hello"))     # Output: Unsupported type
