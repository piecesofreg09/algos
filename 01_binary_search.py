def bii(lis, target):
    left = 0
    right = len(lis) - 1
    
    res = -1
    while left <= right:
        med = (left + right) // 2
        if lis[med] == target:
            return med
        elif lis[med] < target:
            left = med + 1
        else:
            right = med - 1
    return res

arr = [1, 2, 3, 4, 5, 6, 7, 8]
for idd, ele in enumerate(arr):
    t = ele 
    found = bii(arr, t)
    print(str(idd == found) + ' found ' + str(ele) + ' at ' + str(found))
