# bubble sort start from index 0 and moves through an array but iteratively
# swapping elements that are to the right where the right element is smaller than the ith element


def bubbleSort(array):
    # array is the unsorted array
    temp = 0;  #this is a temporary variable to hold the information of the element being swapped

    #loop through n elements in the array
    for i in range(len(array)):
        #loop through each element till index i is in the correct position
        #we know the the ith elements from the end are in position due to the earlier iterations
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1] : #if element to the right is bigger swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp




