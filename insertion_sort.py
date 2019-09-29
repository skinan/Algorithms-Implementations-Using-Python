#!/usr/bin/env
# Python script to perform Insertion Sort and Binary Insertion Sort on a given 1D given_array or list.
# Worst Case Complexity O(n^2)


def binary_search(given_array, key, starting_index, ending_index):
    """ Using binary search method to find the accurate(inplace) place for 'key'
    to reduce the complexity for comparisons of insertion sort"""
    if starting_index == ending_index:
        if given_array[starting_index] > key:
            return starting_index
        else:
            return starting_index + 1
    if starting_index > ending_index:
        return starting_index

    # Binary Search process starts from here.
    mid = (starting_index + ending_index) // 2
    if given_array[mid] < key:
        return binary_search(given_array, key, mid + 1, ending_index)
    elif given_array[mid] > key:
        return binary_search(given_array, key, starting_index, mid)
    elif given_array[mid] == key:
        return mid


def binary_insertion_sort(given_array):  # Function for Binary Insertion Sort
    for i in range(1, len(given_array)):
        key = given_array[i]
        j = binary_search(given_array, key, 0, i - 1)  # Use of binary search to find inplace for the key.

        while i > j:
            given_array[i] = given_array[i - 1]
            i = i - 1
        given_array[j] = key


def insertion_sort(given_array):  # Function for Insertion Sort
    for i in range(1, len(given_array)):  # (n - 1) passes for n elements in a list.
        key = given_array[i]  # Taking every element in the list as a key in every iteration.
        j = i - 1
        while j >= 0 and key < given_array[j]:
            given_array[j + 1] = given_array[j]
            j = j - 1
        given_array[j + 1] = key


def main():
    given_array: list = [8, 2, 4, 9, 3, 6]  # Test Array / List
    insertion_sort(given_array)  # Returns a sorted list in ascending order.
    print("Insertion Sort\n" + "Given Array/list: ", given_array)
    print("After Sorting: ", given_array)
    array1: list = [5, 2, 10, 9, 11, 6]  # Test Array / List
    binary_insertion_sort(array1)  # Returns a sorted list in ascending order.
    print("Binary Insertion Sort\n"+"Given Array/list: ", array1)
    print("After Sorting: ", array1)


if __name__ == "__main__":
    main()
