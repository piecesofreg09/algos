def bii_insert_left(lis, target):
    '''
    location to insert
    if existed, insert on the left of the first occurrence 
    '''
    left = 0
    right = len(lis) - 1
    
    res = -1
    while left <= right:
        med = (left + right) // 2
        if lis[med] == target:
            if med == 0:
                return med
            else:
                if lis[med-1] != target:
                    return med
                else:
                    right = med - 1
        elif lis[med] < target:
            left = med + 1
        else:
            right = med - 1
    return left

arr = [1,1,1,1,5,5,5,5,9,9,9,9]
print(list(enumerate(arr)))

t = 1
print(bii_insert_left(arr, t))
t = -1
print(bii_insert_left(arr, t))
t = 4
print(bii_insert_left(arr, t))
t = 7
print(bii_insert_left(arr, t))
t = 12
print(bii_insert_left(arr, t))

'''
output:
0
0
4
8
12
'''
