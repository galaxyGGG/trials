def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        val_mid = li[mid]
        if val_mid > val:
            right = mid - 1
        elif val_mid < val:
            left = mid + 1
        else:
            return mid
    else:
        return None

li = [1,2,3,4,5,6,7]
print(binary_search(li,6))

