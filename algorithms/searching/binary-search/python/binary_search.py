def find_item(aList, item):
    start = 0
    end = len(aList) - 1
    while end >= start:
        middle = start + (end - start) // 2
        # if the item at the middle
        if aList[middle] == item:
            return middle
        # if item greater than middle, ignore left half
        if item > aList[middle]:
            start = middle + 1
        else: # if item less than middle, ignore right half
            end = middle - 1

    return -1


myList = [1, 2, 3, 4, 5]
print(find_item(myList, 5))