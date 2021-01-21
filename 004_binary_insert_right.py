def bii_insert_right(lis, target):
    '''
    location to insert
    if existed, insert on the right of the last occurrence 
    '''
    left = 0
    right = len(lis) - 1
    
    res = -1
    while left <= right:
        med = (left + right) // 2
        if lis[med] == target:
            if med == len(lis) - 1:
                return med + 1
            else:
                if lis[med + 1] != target:
                    return med + 1
                else:
                    left = med + 1
        elif lis[med] < target:
            left = med + 1
        else:
            right = med - 1
    
    return left




arr = [1,1,1,1,5,5,5,5,9,9,9,9]
print(list(enumerate(arr)))
t = 0
print(bii_insert_right(arr, t))
t = 1
print(bii_insert_right(arr, t))
t = 2
print(bii_insert_right(arr, t))
t = 5
print(bii_insert_right(arr, t))
t = 7
print(bii_insert_right(arr, t))
t = 8
print(bii_insert_right(arr, t))
t = 9
print(bii_insert_right(arr, t))
t = 13
print(bii_insert_right(arr, t))

'''
output:
0
4
4
8
8
8
12
12
'''
