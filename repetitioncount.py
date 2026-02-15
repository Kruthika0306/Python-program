from collections import Counter

def count_occurrences(lst):
    return Counter(lst)

print(count_occurrences([1, 2, 2, 3, 3, 3]))