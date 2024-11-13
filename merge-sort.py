def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    leftSorted = mergeSort(leftHalf)
    rightSorted = mergeSort(rightHalf)

    return merge(leftSorted, rightSorted)


def merge(left, right):
    sortedArray = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i += 1
        else:
            sortedArray.append(right[j])
            j += 1

    sortedArray.extend(left[i:])
    sortedArray.extend(right[j:]) 