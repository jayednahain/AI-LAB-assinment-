def find_number_index(nums_list,n):
    return [idx for idx, i in enumerate(nums_list) if i == n]



print(find_number_index([1,2,3,4,5,2], 2))
print(find_number_index([3,1,2,3,4,5,6,3,3], 3))
print(find_number_index([1,2,3,-4,5,2,-4], -4))