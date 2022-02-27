from multipledispatch import dispatch

# the pivot is the last index
def partition(arr, low, high):
    i = low-1 #index of low element
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] # put on the left side everything smaller then pivot
    arr[i+1],arr[high] = arr[high],arr[i+1] # put pivot in the right place
    return (i+1)

    

@dispatch(list)
def quicksort(arr):
    quicksort(arr, 0, len(arr)-1)
    
@dispatch(list, int, int)
def quicksort(arr, low, high):
    if len(arr) <= 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, 0, pi-1)
        quicksort(arr, pi, high)


if __name__ == "__main__":
    arr = [1,3,2,15,4,1.5]
    quicksort(arr)
    print(arr)
