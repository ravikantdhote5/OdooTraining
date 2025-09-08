
#List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x * 2 for x in numbers if x % 2 != 0]
print(result)  # Output: [2, 6, 10, 14, 18]