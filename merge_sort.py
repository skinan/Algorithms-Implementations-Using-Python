#!/usr/bin/python
# Python script to perform Merge Sort on a given array/ list / matrix(1D)
# Worst Case Complexity O(n*log(n))

import math


def merge(array_list, start_index, mid, end_index):
    length_left = (mid - start_index) + 1  # Length of a left sublist.
    length_right = end_index - mid  # Length of right sublist.

    left_sublist = [None]*length_left  # Create a left sublist.
    right_sublist = [None]*length_right  # Create a right sublist.

    # Assign elements to left and right sublist.
    for i in range(0, length_left):
        left_sublist[i] = array_list[start_index + i]
    for j in range(0, length_right):
        right_sublist[j] = array_list[mid + j + 1]

    # Append "infinity" as the last element of two sublist.
    left_sublist.append(math.inf)
    right_sublist.append(math.inf)
    
    i = j = 0

    # Finally sort elements by comparing elements of left and right sublist.
    for k in range(start_index, end_index + 1):
        if left_sublist[i] <= right_sublist[j]:
            array_list[k] = left_sublist[i]
            i = i + 1
        else:
            array_list[k] = right_sublist[j]
            j = j + 1


def merge_sort(array_list, start_index, end_index):
    if start_index < end_index:  # The condition is true until only 1 element left in the list.
        mid = (start_index + end_index)//2  # Generate a value for mid.
        merge_sort(array_list, start_index, mid)  # Create left sublist (n/2).
        merge_sort(array_list, mid + 1, end_index)  # Create right sublist (n/2).
        merge(array_list, start_index, mid, end_index)  # Merge created sub-lists in recursive manner.


def main():
    array_list: list = [8, 2, 4, 9, 3, 6]  # Test Array / List
    print("Given Array/List: ", array_list)
    merge_sort(array_list, 0, len(array_list) - 1)
    print("After Sorting: ", array_list)


if __name__ == "__main__":
    main()
