
def bubble_sort(given_list):
    for i in range(0, len(given_list)):
        for j in range(0, len(given_list) - (i + 1)):  # start of for loop to compare and interchange elements
            if given_list[j] > given_list[j + 1]:  # Compare and if previous element is getter than next element.
                given_list[j + 1], given_list[j] = given_list[j], given_list[j + 1]  # Swap!        


def main():
    given_list = list(map(int, input("Enter Elements: ").split(" ")))
    print("Given List : ", *given_list)
    bubble_sort(given_list)
    print("After Bubble Sort :", *given_list)


if __name__ == "__main__":
    main()
