def reverseArray(n,arr):
    i = 0
    j = n-1
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1
    return arr

## def reverse(arr):
##      rev = arr[::-1]
##      return rev