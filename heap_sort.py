#!/usr/bin/env
# Python script to perform Heap Sort on a given 1D given_array or list.
# Time Complexity: O(n * log(n))


def heapify(given_array, i, n):
    root = i
    left_node = (2 * i) + 1
    right_node = (2 * i) + 2

    """ Conditions below are set to build max-heap """

    if left_node <= n:
        if given_array[root] <= given_array[left_node]:
            given_array[root], given_array[left_node] = given_array[left_node], given_array[root]  # Swap!

        heapify(given_array, left_node, n)  # Recursive call to build max heap.

        if given_array[root] <= given_array[left_node]:
            given_array[root], given_array[left_node] = given_array[left_node], given_array[root]  # Swap!

    if right_node <= n:
        if given_array[root] <= given_array[right_node]:
            given_array[root], given_array[right_node] = given_array[right_node], given_array[root]  # Swap!

        heapify(given_array, right_node, n)  # Recursive call to build max heap.

        if given_array[root] <= given_array[right_node]:
            given_array[root], given_array[right_node] = given_array[right_node], given_array[root]  # Swap!


def heap_sort(given_array):
    n = len(given_array) - 1  # Find the index of last element in array.
    while n >= 0:
        heapify(given_array, 0, n)
        # Swap the last element of heap with first element.
        given_array[0], given_array[n] = given_array[n], given_array[0]
        n -= 1  # Reduce length of heap after every iteration.


def main():
    given_array = [5, 4, 12, 3, 8, 9, 11, 6, 50, -1, -5,  14]
    print("Given Array:", given_array)
    heap_sort(given_array)
    print("After Sorting In Increasing Order: ", given_array)


if __name__ == "__main__":
    main()
