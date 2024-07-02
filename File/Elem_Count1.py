#Elements Count Without Counter()
def count_occurrences(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Example usage
example_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(count_occurrences(example_list))
