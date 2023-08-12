def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr=[2,7,9,0, 0, 4,5,6,]
print(bubbleSort(arr))
