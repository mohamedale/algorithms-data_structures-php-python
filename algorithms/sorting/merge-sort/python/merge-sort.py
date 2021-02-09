"""
    this merge type is stable because we sorted in the same array
"""
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        # get left part
        leftP = arr[:mid]
        # get right part
        rightP = arr[mid:]

        # do recursion
        leftP = mergeSort(leftP)
        rightP = mergeSort(rightP)

        # comparing process
        i = j = k = 0
        while i < len(leftP) and j < len(rightP):
            if leftP[i] < rightP[j]:
                arr[k] = leftP[i]
                i += 1  # for left count steps
            else:
                arr[k] = rightP[j]
                j += 1  # for right count steps
            k += 1

        while i < len(leftP):
            arr[k] = leftP[i]
            i += 1
            k += 1

        while j < len(rightP):
            arr[k] = rightP[j]
            j += 1
            k += 1

    return arr


print(mergeSort([0, 4, 1, 9, 8, 2]))
