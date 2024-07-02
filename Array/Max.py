def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

array = [1, 3, 7, 0, -5, 7]
print(find_max(array))