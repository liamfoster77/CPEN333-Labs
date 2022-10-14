#student name:      Liam Foster
#student number:    40199382

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    
    def partition(low: int, high: int, arr: list) -> int:
        """
           Description: Helper function for Quick Sort algorithm. 
           Function: Partitions the array about a pivot and puts the
           pivot in its correct position. Puts all elements smaller 
           than the pivot before the pivot and all elements greater
           than the pivot after the pivot
           
           low: starting index
           high: ending index
           arr: list to sort
        """
        # chooses rightmost element as pivot
        pivot = arr[high]
        # index of greater element
        i = low - 1

        # loop through all elements from low to high
        for j in range(low, high):
            # compare each element with the pivot
            if arr[j] <= pivot:
                # if element smaller than the pivot is found, 
                # swap it with greater element pointed by i
                i += 1
                (arr[i], arr[j]) = (arr[j], arr[i])

        # swap pivot with greater element pointed by i
        (arr[i+1], arr[high]) = (arr[high], arr[i+1])
        # return position of partition
        return i + 1
    
    
    def sortHalf(low: int, high: int, destination: list) -> None:
        """
           Description: Recursive sorting function that uses a Quick 
           Sort algorithm
           Function: Calls partition to find a pivot element and 
           recursively calls itself to sort the destination list

           low: starting index
           high: ending index
           destination: list to sort
        """
        if (low<high):

            # Find pivot element such that smaller elements are to the left
            # and larger elements are to the right
            pi = partition(low, high, destination)
            
            # Recursive calls on the left and right sides of pivot
            sortHalf(low, pi - 1, destination)
            sortHalf(pi + 1, high, destination)


    # Driver code
    
    # check if firstHalf is True or not and assign the start and end indices
    # and the destination array address to their respective values
    if firstHalf == True:
        start = 0
        end = int(len(testcase)/2)
        global sortedFirstHalf 
        sortedFirstHalf = testcase[start:end].copy()
        sortHalf(0,len(sortedFirstHalf)-1,sortedFirstHalf)
    elif firstHalf == False:
        start = int(len(testcase)/2)
        end = int(len(testcase))
        global sortedSecondHalf
        sortedSecondHalf = testcase[start:end].copy()
        sortHalf(0,len(sortedSecondHalf)-1,sortedSecondHalf)
    
    
    # call recursive sorting function
    


def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    
    i = 0
    j = 0
    end = len(sortedFirstHalf)

    while i < end and j < end:
        if sortedFirstHalf[i] <= sortedSecondHalf[j]:
            SortedFullList.append(sortedFirstHalf[i])
            i += 1
        else:
            SortedFullList.append(sortedSecondHalf[j])
            j += 1
        
    if i >= end:
        while j < end:
            SortedFullList.append(sortedSecondHalf[j])
            j += 1
    else:
        while i < end:
            SortedFullList.append(sortedFirstHalf[i])
            i += 1




if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #creating half sort threads
    firstHalf = threading.Thread(target=sortingWorker,args=(True,))
    secondHalf = threading.Thread(target=sortingWorker,args=(False,))
    firstHalf.start()
    secondHalf.start()
    #join the halves before merging
    firstHalf.join()
    secondHalf.join()
    
    merge = threading.Thread(target=mergingWorker)
    merge.start() 
    merge.join()
    
    #as a simple test, printing the final sorted list
    print("The final sorted list is", SortedFullList)