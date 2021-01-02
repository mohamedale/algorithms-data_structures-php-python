def bubble_sort(aList):
    for i in range(len(aList)):
        swapped = False; # for Optimized Implementation:
        for m in range(len(aList) - i -1):
            if aList[m] > aList[m+1]:
                aList[m], aList[m+1] = aList[m+1], aList[m]
                swapped = True

        if swapped == False:
            break
    return aList

myList = [7, 5, 2, 3, 8]
print(bubble_sort(myList))