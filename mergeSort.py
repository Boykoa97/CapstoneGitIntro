#mergesort is a recursive function that breaks an array into smaller pieces
#then when it only has to compare two elements it sorts those two elements and afterwards combines each of these small
#pieces into a sorted array

def mergeSort(array):
    length = len(array)

    if length == 2:
        swap = 0
        if array[0] > array[1]:
            swap = array[0]
            array[0] = array[1]
            array[1] = swap
    elif length == 1:
        #do nothing because there is only one element
        swap = 0
    else:
        mid = int(length/2)

        print(array[:mid])
        print(array[mid:])
        leftSide = mergeSort(array[:mid])
        rightSide = mergeSort(array[mid:])

        leftCounter = 0
        rightCounter = 0
        for i in range(0,length):
            if leftCounter < len(leftSide) and rightCounter < len(rightSide):
                if leftSide[leftCounter] < rightSide[rightCounter]:
                    array[i] = leftSide[leftCounter]
                    leftCounter+=1
                else:
                    array[i] = rightSide[rightCounter]
                    rightCounter+=1
            else:
                if rightCounter == len(rightSide):
                    array[i] = leftSide[leftCounter]
                    leftCounter+=1
                else:
                    array[i] = rightSide[rightCounter]
                    rightCounter += 1

    return array

testEven = [2, 4, 3, 1, 7, 8, 12, 11, 10,15]
testOdd = [2,4,3,1,7,8,12,11,10]

testEven = mergeSort(testEven)
testOdd = mergeSort(testOdd)

print(testOdd)
print(testEven)

