#!/usr/bin/python
# Python script for basic Insertion Sort and Binary Insertion Sort.


def binary_search(array, key, start, end):
    """ Using binary search method to find the accurate place for 'key'
    to reduce the complexity for comparisons of insertion sort"""
    if start == end:
        if array[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if array[mid] < key:
        return binary_search(array, key, mid + 1, end)
    elif array[mid] > key:
        return binary_search(array, key, start, mid)
    elif array[mid] == key:
        return mid


def binary_insertion_sort(array):  # Function for Binary Insertion Sort
    for i in range(1, len(array)):
        key = array[i]
        j = binary_search(array, key, 0, i - 1)  # Use of binary search to find inplace for the key.

        while i > j:
            array[i] = array[i - 1]
            i = i - 1
        array[j] = key
    return array


def insertion_sort(array):  # Function for Insertion Sort
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def main():
    array: list = [8, 2, 4, 9, 3, 6]  # Test Array / List
    print(insertion_sort(array))  # Returns a sorted list in ascending order.
    print(binary_insertion_sort(array))  # Returns a sorted list in ascending order.


if __name__ == "__main__":
    main()
