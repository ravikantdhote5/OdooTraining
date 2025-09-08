def print_pattern(n):
    for i in range(n, 0, -1):  # Count down from n to 1
        numbers = [str(x) for x in range(i, n+1)]  # Numbers from i to n
        print(','.join(numbers))  # Join with commas and print

# Example usage
n = 6
print_pattern(n)