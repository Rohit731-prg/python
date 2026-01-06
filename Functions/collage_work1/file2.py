# selection sort in python

def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        loc = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]
    return arr

ls = [5, 2, 9, 1, 5, 6]
print("Original list:", ls)
result = selection_sort(ls)
print("Sorted list:", selection_sort(ls))