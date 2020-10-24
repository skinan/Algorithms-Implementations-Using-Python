from math import floor


def binary_search(input_list, search):
    check = False 
    low = 0
    n = len(input_list)
    high = n - 1
    
    while high > low:
        mid = floor((high + low - 1) / 2)
        if input_list[mid] == search:
            check = True
            break
        elif input_list[mid] > search:
            high = mid - 1
        else:
            low = mid + 1

    return check


def main():
    input_list = [1, 2, 3, 5, 8, 9, 11]
    search = 8  # Search For
    check = binary_search(input_list, search)
    if check:
        print("Hurray! Found it!")
    else:
        print("Sorry! This is not found.")

    
if __name__ == "__main__":
    main()

