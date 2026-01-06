# bubble sort in Python

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

ls = [5, 2, 9, 1, 5, 6]
print("Original list:", ls)
result = bubble_sort(ls)
print("Sorted list:", bubble_sort(ls))