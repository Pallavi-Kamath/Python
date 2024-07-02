def Find_min(array):
    
    minimun= array[0]
    for num in array:
        if num< array[0]:
            minimun=num
    return minimun

m=Find_min([1,2,3,-1,5])
print(m)