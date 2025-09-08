#Sorting based on string length
def sort_by_length(strings):
    return sorted(strings, key=lambda s: len(s))

names = ['deepak', 'aman', 'sam', 'naman', 'mohit']
sorted_names = sort_by_length(names)
print(sorted_names)         #['sam', 'aman', 'naman', 'mohit', 'deepak']