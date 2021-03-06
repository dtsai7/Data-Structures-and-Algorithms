def shellsort(array):
    n = len(array)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j-= gap
            array[j] = temp
        gap //=2


arr = [34,55,21,76,83,32,94,62,12]
shellsort(arr)
print(arr)
