#!/usr/bin/env
# Python script to perform Merge Sort on a given array/ list / matrix(1D)
# Worst Case Complexity O(n*log(n))

import math


def merge(given_array, start_index, mid, end_index):
    length_left = (mid - start_index) + 1  # Length of a left sublist.
    length_right = end_index - mid  # Length of right sublist.

    left_sublist = [None]*length_left  # Create a left sublist.
    right_sublist = [None]*length_right  # Create a right sublist.

    # Assign elements to left and right sublists.
    for i in range(0, length_left):
        left_sublist[i] = given_array[start_index + i]
    for j in range(0, length_right):
        right_sublist[j] = given_array[mid + j + 1]

    # Append "infinity" as the last element of two sub-lists.
    left_sublist.append(math.inf)
    right_sublist.append(math.inf)

    i = j = 0

    # Finally sort elements by comparing elements of left and right sublists.
    for k in range(start_index, end_index + 1):
        if left_sublist[i] <= right_sublist[j]:
            given_array[k] = left_sublist[i]
            i = i + 1
        else:
            given_array[k] = right_sublist[j]
            j = j + 1


def merge_sort(given_array, start_index, end_index):
    if start_index < end_index:  # The condition is true until only 1 element left in the list.
        mid = (start_index + end_index)//2  # Generate a value for mid.
        merge_sort(given_array, start_index, mid)  # Create left sublist (n/2).
        merge_sort(given_array, mid + 1, end_index)  # Create right sublist (n/2).
        merge(given_array, start_index, mid, end_index)  # Merge created sub-lists in recursive manner.


def main():
    given_array: list = list(map(int, input().split(" ")))  # Test Array / List
    print("Given Array/List: ", given_array)
    merge_sort(given_array, 0, len(given_array) - 1)
    print("After Sorting: ", given_array)


if __name__ == "__main__":
    main()
