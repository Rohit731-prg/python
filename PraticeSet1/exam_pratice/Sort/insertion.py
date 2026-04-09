# insertion sort implementation

def insertion_sort(arr) -> list:
    length = len(arr)
    for i in range(length):
        min = arr[i]
        loc = i

        for j in range(i + 1, length):
            if arr[j] < min:
                min = arr[j]
                loc = j

        arr[i], arr[loc] = arr[loc], arr[i]
    return arr

ls = [9, 2, 7, 1, 5, 6]
print("Original list:", ls)
sorted_ls = insertion_sort(ls)
print("Sorted list:", sorted_ls)