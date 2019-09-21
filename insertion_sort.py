def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    elif arr[mid] == key:
        return mid


def binary_insertion_sort(arr):  # Function for Binary Insertion Sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i - 1)

        while i > j:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[j] = key
    return arr


def insertion_sort(arr):  # Function for Insertion Sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def main():
    l: list = [8, 2, 4, 9, 3, 6]  # Test Array / List
    print(insertion_sort(l))  # Returns a sorted list in ascending order.
    print(binary_insertion_sort(l))  # Returns a sorted list in ascending order.


if __name__ == "__main__":
    main()
