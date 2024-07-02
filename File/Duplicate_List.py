#remove Duplicate from list

def remove_duplicates(nums):
    return list(set(nums))

# Example usage
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

#Convert the list to a set, which automatically removes duplicates because sets cannot contain duplicate elements.