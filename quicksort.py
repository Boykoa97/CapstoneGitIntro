#doing quicksort using the first element as the pivot
def quickSort(array, low, high):
    #start index is low and end index is high
    if low < high:
        #pivot is partitioning index, array[pivot] is now in proper place
        pivot = partition(array,low,high)

        quickSort(array,low, pivot-1) #elements smaller than pivot that need sorting
        quickSort(array,pivot+1,high) #elements larger than pivot that need sorting

#this takes the first element as the pivot and moves it to the correct location in the sorted array
#all elements smaller than the pivot are moved to the left and all larger elements are moved to the right
def partition(array,low,high):
    pivot = array[low]
    i = high + 1 #index of larger element

    for j in range(high,low,-1):
        #if curr element is > than pivot
        if array[j] > pivot:
            i-=1 #decrement index of larger element
            swap = array[i]
            array[i] = array[j]
            array[j]=swap
    swap = array[i-1]
    array[i-1] = array[low]
    array[low] = swap
    return i-1


testEven = [2,4,5,6,1,7]
testOdd = [2,4,5,6,3,10,1,7,8]

quickSort(testEven,0,len(testEven)-1)
quickSort(testOdd,0,len(testOdd)-1)

print(testEven)
print(testOdd)