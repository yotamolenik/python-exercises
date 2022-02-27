from multipledispatch import dispatch

def partition(arr, low, high):
        pivot = arr[high]
        i = low-1
        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
  
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

@dispatch(list)
def quicksort(arr):
    quicksort(arr, 0, len(arr)-1)
    
@dispatch(list, int, int)
def quicksort(arr, low, high):
    print(arr[low: high])
    if len(arr) <= 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi, high)

if __name__ == "__main__":
    arr = [3,7,2,17,5,4,1]
    # quicksort(arr)
    print(arr[2:3])
    