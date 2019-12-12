#!/usr/bin/env
# Python script to find maximum and minimum element from array using divide and conquer.
# Run Time Complexity: Worst case O(n), Average Case: log(n)


import math


def find_min_max(given_array, starting_index, ending_index):
    global maximum  # Global Variable Declaration To Make Changes In This Scope.
    global minimum  # Global Variable Declaration To Make Changes In This Scope.
    # Divide Part
    if starting_index < ending_index:
        mid_index = (starting_index + ending_index) // 2
        find_min_max(given_array, starting_index, mid_index)
        find_min_max(given_array, mid_index + 1, ending_index)

    # Pair Comparison Part After Divide
    if given_array[ending_index] > maximum:
        maximum = given_array[ending_index]
    if given_array[ending_index] < minimum:
        minimum = given_array[ending_index]


def main():
    given_array = [1000, 11, 445, 1, 330, 3000, -2, 3]
    find_min_max(given_array, 0, len(given_array) - 1)
    print("Given Array:", given_array)
    print("Maximum of Given Array: ", maximum)
    print("Minimum of Given Array: ", minimum)


if __name__ == '__main__':
    minimum = math.inf
    maximum = - math.inf
    main()
