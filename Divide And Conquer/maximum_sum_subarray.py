#!/usr/bin/env
# Problem: Finding A Maximum Sum Contiguous Sub Array From An Given List/Array.(Using Divide & Conquer)
# Complexity, when "Divide & Conquer" method is used: O(n*log(n))
import math


def max_crossing_subarray(given_array, start_index, mid_index, end_index):
    """Function To Calculate The Mid Crossing Sub Array Sum"""

    max_left_sum = - math.inf  # Used For Sentinel Value
    max_right_sum = - math.inf  # Used For Sentinel Value

    cross_start = None  # Just used for variable pre assignment.
    cross_end = None  # Just used for variable pre assignment.

    temp_sum = 0
    # Find Max Sub Array in Left Part
    for i in reversed(range(start_index, mid_index + 1)):
        temp_sum = temp_sum + given_array[i]

        # Keep track of the max sum
        if temp_sum > max_left_sum:
            max_left_sum = temp_sum
            cross_start = i

    temp_sum = 0
    # Find Max Sub Array In Right Part
    for j in range(mid_index + 1, end_index + 1):
        temp_sum = temp_sum + given_array[j]

        # Keep track of the max sum
        if temp_sum > max_right_sum:
            max_right_sum = temp_sum
            cross_end = j

    max_sum_ans = max_left_sum + max_right_sum  # Max From This Sub Array.
    return cross_start, cross_end, max_sum_ans


def maximum_sum_subarray(given_array, start_index, end_index):
    if start_index >= end_index:
        return start_index, end_index, given_array[start_index]

    mid_index = (start_index + end_index) // 2
    left_start, left_end, left_sum = maximum_sum_subarray(given_array, start_index, mid_index)  # max value (left)
    right_start, right_end, right_sum = maximum_sum_subarray(given_array, mid_index + 1, end_index)  # max value (right)

    # max value of mid crossing sublist.
    cross_start, cross_end, mid_cross_sum = max_crossing_subarray(given_array, start_index, mid_index, end_index)

    if max(left_sum, right_sum, mid_cross_sum) == left_sum:
        return left_start, left_end, left_sum  # return answers
    elif max(left_sum, right_sum, mid_cross_sum) == right_sum:
        return right_start, right_end, right_sum
    else:
        return cross_start, cross_end, mid_cross_sum


def main():
    given_array = [-2, -5, 6, -2, -3, 1, 5, -6]
    print("Given Array:  ", given_array)
    ans_start_index, ans_end_index, ans_sum = maximum_sum_subarray(given_array, 0, len(given_array) - 1)
    print("Maximum Sum of Contiguous Sub Array:", ans_sum)
    print("Sub Array Index:", ans_start_index + 1, "to", ans_end_index + 1)


if __name__ == "__main__":
    main()
