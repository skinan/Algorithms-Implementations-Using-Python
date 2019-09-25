#!/usr/bin/env
# Problem: Finding a 1D peak in given array if it exists. (Using Divide & Conquer)
# Complexity when "Divide & Conquer" method is used: O(log(n))

import math


def find_peak(array_list, starting_index, ending_index):
    # Using binary search (divide & conquer) to reduce complexity of the algorithm.
    mid = (starting_index + ending_index)//2
    if array_list[mid - 1] <= array_list[mid] >= array_list[mid + 1]:
        return array_list[mid]
    elif array_list[mid-1] > array_list[mid]:
        return find_peak(array_list, starting_index, mid - 1)
    elif array_list[mid + 1] > array_list[mid]:
        return find_peak(array_list, mid + 1, ending_index)


def main():
    array_list = [8, 2, 4, 6, 9, 3]
    array_length = len(array_list)  # Size of the given array.
    # Use of a sentinel value to avoid index error in case of strictly increasing or decreasing order.
    array_list.insert(0, -math.inf)
    array_list.append(-math.inf)

    # Call the function and show the result.
    result = find_peak(array_list, 1, array_length - 1)
    if result:
        print("A 1D peak is: ", result)
    else:   # This 'else' condition will never run as there exists a peak always in an 1D array.
        print("There is no 1D peak in the array.")


if __name__ == "__main__":
    main()
