aList = [5, 7, 8, 2, 3, 1, 6]

for i in range(1, len(aList)):
    key = aList[i]
    j = i - 1

    while j >= 0 and aList[j] > key:
        aList[j+1] = aList[j]
        j -= 1

    aList[j+1] = key

print(aList)