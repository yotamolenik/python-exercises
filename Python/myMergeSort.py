
def merge(leftarr, rightarr):
    leftsize = len(leftarr)
    rightsize = len(rightarr)
    merged = []
    i, j = 0, 0
    while i < leftsize and j < rightsize:
        if leftarr[i] <= rightarr[j]:
            merged.append(leftarr[i])
            i += 1
        else:
            merged.append(rightarr[j])
            j += 1
    # after the while, either i or j went out of bounds (exactly one of them)
    if i == leftsize:
        merged.extend(rightarr[j:])
    else:
        merged.extend((leftarr[i:]))
    return merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    leftarr = arr[:m]
    rightarr = arr[m:]
    sortedleft = mergesort(leftarr)
    sortedright = mergesort(rightarr)
    return merge(sortedleft, sortedright)


if __name__ == "__main__":
    arr = [4, 3, 5, 7, 6, 1, 5]
    sortedarr = mergesort(arr)
    print(arr)
    print(sortedarr)
