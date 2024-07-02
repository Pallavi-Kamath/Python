#merge 2 list into single sorted list
def merge_and_sort_lists(list1, list2):
   
    combined_list = list1 + list2
    
    combined_list.sort()
    return combined_list

print(merge_and_sort_lists([5,4,6], [1,2,3]))
print(merge_and_sort_lists([2,5,1], [8,2,4]))