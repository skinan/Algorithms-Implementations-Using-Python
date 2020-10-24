def counting_sort(arr):
    temp = [0] * (max(arr) + 1)
    for _ in arr:
        temp[_] = temp[_] + 1

    result_array = []
    for index, element in enumerate(temp):
        j = 0
        while j < element:
            result_array.append(index)
            j += 1

    return result_array


def main():
    arr = [4, 5, 3, 3, 10, 11]
    print("Sorted Array: ", counting_sort(arr))


if __name__ == "__main__":
    main()
