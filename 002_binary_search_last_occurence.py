def bii_last(lis, target):
    left = 0
    right = len(lis) - 1
    
    res = -1
    while left <= right:
        med = (left + right) // 2
        if lis[med] == target:
            if med == len(lis) - 1:
                return med
            else:
                if lis[med+1] != target:
                    return med
                else:
                    left = med + 1
        elif lis[med] < target:
            left = med + 1
        else:
            right = med - 1
    return res

arr = [1,1,1,1,2,2,2,2,3,4,5,6,6,6,6,7, 8]
t = 6
print(list(enumerate(arr)))
print(bii_last(arr, t))
