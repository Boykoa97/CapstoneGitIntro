#This file is just to compile all the feature branches

from bubblesort import bubbleSort
from mergeSort import mergeSort
from quicksort import quickSort


testBubble = [3,10,40,20,30,4,1]
testMerge = [100,5,68,3,1,10]
testQuick = [4,15,23,1,11,22]

bubbleSort(testBubble)
print("Here is the the sorted array using bubble sort")
print(testBubble)
mergeSort(testMerge)
print("Here is the sorted array using Merge sort")
print(testMerge)
quickSort(testQuick,0,len(testQuick)-1)
print("Here is the sorted array using quick sort")
print(testQuick)
