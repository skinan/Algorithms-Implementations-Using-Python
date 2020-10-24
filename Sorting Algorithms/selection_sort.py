def selection_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr


def main():
    arr = [1, 4, -3, 9, 5]
    print("Selection Sort: ", selection_sort(arr))


if __name__ == "__main__":
    main()
