

def partition(given_array, start_index, end_index):
    i = start_index - 1

    pivot = given_array[end_index]
    for j in range(start_index, end_index):
        if given_array[j] < pivot:
            i += 1
            given_array[i], given_array[j] = given_array[j], given_array[i]

    given_array[i + 1], given_array[end_index] = given_array[end_index], given_array[i + 1]
    return i + 1


def quick_sort(given_array, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(given_array, start_index, end_index)
        quick_sort(given_array, start_index, partition_index - 1)
        quick_sort(given_array, partition_index + 1, end_index)


def main():
    given_array =[7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort(given_array, 0, len(given_array) -1)
    print("After Sorting: ", *given_array)


if __name__ == "__main__":
    main()