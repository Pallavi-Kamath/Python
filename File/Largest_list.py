def largest_list(list):
    largest = list[0];
    
    for i in list:
        if i > largest:
            largest= i
    
    return largest

print(largest_list([10,2,3,4,5]))