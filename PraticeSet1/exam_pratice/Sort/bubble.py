# bubble sort implementation

def bubble_sort(arr) -> list:
    length = len(arr)
    count = 0
    for i in range(length):
        count += 1
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

ls = [9, 2, 7, 1, 5, 6]
print("Original list:", ls)
sorted_ls = bubble_sort(ls)
print("Sorted list:", sorted_ls)