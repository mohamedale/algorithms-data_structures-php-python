def selection_sort(aList):
    for i in range(len(aList)):
        lowNumIndex = i
        for j in range(i+1, len(aList)):
            if aList[j] < aList[lowNumIndex]:
                lowNumIndex = j

        if aList[i] > aList[lowNumIndex]:
            tmp = aList[i]
            aList[i] = aList[lowNumIndex]
            aList[lowNumIndex] = tmp

    return aList

myList = [5, 7, 9, 4, 3, 8, 2]
print(selection_sort(myList))