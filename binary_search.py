# 二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] == item):
            return mid
        elif (list[mid] < item):
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_first_equal_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] == item):
            if mid == 0 or list[mid - 1] != item:
                return mid
            else:
                high = mid - 1
        elif (list[mid] < item):
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_last_equal_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] == item):
            if mid == len(list) - 1 or list[mid + 1] != item:
                return mid
            else:
                low = mid + 1
        elif (list[mid] < item):
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_first_larger_or_equal_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] == item):
            if mid == 0 or list[mid - 1] != item:
                return mid
            else:
                high = mid - 1
        elif (list[mid] < item):
            low = mid + 1
        else:
            if mid == 0 or list[mid - 1] < item:
                return mid
            else:
                high = mid - 1

    return -1


def better_find_first_larger_or_equal_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] >= item):
            if mid == 0 or list[mid - 1] < item:
                return mid
            else:
                high = mid - 1
        elif (list[mid] < item):
            low = mid + 1

    return -1


def find_last_smaller_equal_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        print(low, high, mid, list[mid])
        if (list[mid] <= item):
            if mid == len(list) - 1 or list[mid + 1] > item:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1

    return -1


def recursion_binary_search(list, item, start, end):
    if (start > end):
        return -1
    mid = int((end + start) / 2)

    print(start, end, mid, list[mid])

    if (list[mid] == item):
        return mid
    elif list[mid] < item:
        return recursion_binary_search(list, item, mid + 1, end)
    else:
        return recursion_binary_search(list, item, start, mid - 1)


# print(binary_search([1, 10, 12, 23, 29, 34, 100], 23))

# print(recursion_binary_search([1, 10, 12, 23, 29, 34, 100], 23, 0, 6))

# print(find_first_binary_search([1, 10, 12, 12, 23, 23, 23, 29, 34, 100], 23))

# print(find_last_binary_search([1, 10, 12, 12, 12, 23, 23, 23, 23, 29, 34, 34, 100], 23))

# print(find_first_larger_or_equal_binary_search([1, 10, 12, 12, 12, 23, 23, 23, 23, 29, 34, 34, 100], 24))

print(find_last_smaller_equal_binary_search([1, 10, 12, 12, 12, 23, 23, 23, 23, 29, 34, 34, 100], 11))

