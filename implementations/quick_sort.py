
def partition(arr,start,end,pivot = None): 
    if(pivot is None):
        pivot = arr[end]
    i = start
    j = end-1
    while (i < j):
        if arr[i] > pivot and arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        elif arr[i] > pivot and arr[j] > pivot:
            j -= 1
        elif arr[j] < pivot and arr[i] < pivot:
            i += 1
            if(i == j):
                i += 1
        else:
            i += 1
            j -= 1

    temp = arr[i]
    arr[i] = pivot
    arr[end] = temp
    return i 



def quickSort(arr,start,end): 
    if start < end:
        pivot = partition(arr,start,end) 
        quickSort(arr, start, pivot-1) 
        quickSort(arr, pivot+1, end) 


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print (arr) 



