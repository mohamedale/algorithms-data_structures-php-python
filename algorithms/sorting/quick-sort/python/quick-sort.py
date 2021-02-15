# low  --> Starting index,  high  --> Ending index
def partition(myList, low, high):
    pivot = myList[high]  # to put it in the right position
    i = low - 1  # index of smaller element

    for j in range(low, high):
        # If current element is smaller than the pivot
        if myList[j] < pivot:
            # increment index of smaller element
            i += 1
            # swapping
            myList[i], myList[j] = myList[j], myList[i]

    # swapping
    myList[i + 1], myList[high] = myList[high], myList[i + 1]
    return i + 1


def quick_sort(theList, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(theList, low, high)
        # recursion
        quick_sort(theList, low, pi - 1)  # before pi
        quick_sort(theList, pi + 1, high)  # after pi
    return theList


# this function not required
def sort(entryList):
    return quick_sort(entryList, 0, len(entryList) - 1)


# do sorting
unSortedList = [9, 2, 7, 8, 3, 4]
print(sort(unSortedList))
