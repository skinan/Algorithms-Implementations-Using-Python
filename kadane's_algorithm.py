#!/usr/bin/env
# Problem: Finding A Maximum Sum Contiguous Sub Array An Given List/Array.(Using Kadane's Algorithm)
# Time Complexity: O(n)
# Dynamic Programming
import math


def maximum_sum_subarray(given_array):

    max_till_now = - math.inf  # Using a sentinel value
    current_max = - math.inf   # Using a sentinel value
    for i in range(len(given_array)):
        current_max = max(given_array[i], given_array[i] + current_max)
        max_till_now = max(max_till_now, current_max)

    return max_till_now


def main():
    given_array = [-2, -5, 6, -2, -3, 1, 5, -6]
    print("Given Array:  ", given_array)
    print("Implementing Kadane's Algortihm ")
    print("Maximum Sum of Contiguous Sub Array  : ", maximum_sum_subarray(given_array))


if __name__ == "__main__":
    main()
