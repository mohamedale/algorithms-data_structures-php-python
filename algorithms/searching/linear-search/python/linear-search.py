def linear_search(list, item):
    for index, num in enumerate(list):
        if item == list[index]:
            return index

    return -1 # mean this element not found

myList = [1, 2, 3, 4, 5]
print(linear_search(myList, 5))