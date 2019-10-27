#!/usr/bin/env
# Problem: Finding A Maximum Sum Contiguous Sub Array From An Given List/Array.(Using Divide & Conquer)
# Complexity, when "Divide & Conquer" method is used: O(n*log(n))
import math


def max_crossing_subarray(given_array, start_index, mid_index, end_index):
    max_left = - math.inf  # Used For Sentinel Value
    max_right = - math.inf  # Used For Sentinel Value

    temp_sum = 0
    # Find Max Sub Array in Left Part
    for i in reversed(range(start_index, mid_index + 1)):
        temp_sum = temp_sum + given_array[i]
        max_left = max(max_left, temp_sum)

    temp_sum = 0
    # Find Max Sub Array In Right Part
    for i in range(mid_index + 1, end_index + 1):
        temp_sum = temp_sum + given_array[i]
        max_right = max(max_right, temp_sum)

    max_ans = max_left + max_right  # Max From This Sub Array.
    return max_ans


def maximum_sum_subarray(given_array, start_index, end_index):
    if start_index >= end_index:
        return given_array[start_index]
    mid_index = (start_index + end_index) // 2
    left_sum = maximum_sum_subarray(given_array, start_index, mid_index)  # Get the max sum value of left sublist.
    right_sum = maximum_sum_subarray(given_array, mid_index + 1, end_index)  # Get the max sum value of right sublist.
    mid_cross_sum = max_crossing_subarray(given_array, start_index, mid_index, end_index)  # Get the total(left + right)
    return max(left_sum, right_sum, mid_cross_sum)


def main():
    given_array = [-2, -5, 6, -2, -3, 1, 5, -6]
    print("Maximum Sum of Contiguous Sub Array : ", maximum_sum_subarray(given_array, 0, len(given_array) - 1))


if __name__ == "__main__":
    main()
