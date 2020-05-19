def another_merge_sort(array, start, end):
    if start >= end:
        return

    mid = int((start + end) / 2)
    print(start, end, mid)

    another_merge_sort(array, start, mid)
    another_merge_sort(array, mid + 1, end)

    i = start
    j = mid + 1

    newarray = []
    while(i <= mid and j <= end):
        if array[i] < array[j]:
            newarray.append(array[i])
            i += 1
        else:
            newarray.append(array[j])
            j += 1

    while i <= mid:
        newarray.append(array[i])
        i += 1

    while j <= end:
        newarray.append(array[j])
        j += 1

    index = 0
    i = start
    while i <= end:
        array[i] = newarray[index]
        i += 1
        index += 1


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = int(len(array) / 2)

    left_array = merge_sort(array[0: mid])
    right_array = merge_sort(array[mid: len(array)])

    i = j = index = 0

    while(i < len(left_array) and j < len(right_array)):
        if left_array[i] < right_array[j]:
            array[index] = left_array[i]
            i += 1
        else:
            array[index] = right_array[j]
            j += 1

        index += 1

    while i < len(left_array):
        array[index] = left_array[i]
        i += 1
        index += 1

    while j < len(right_array):
        array[index] = right_array[j]
        j += 1
        index += 1

    return array


# print(merge_sort([0, 19, 19, 48, 1, 5, 38]))

array = [0, 19, 19, 48, 1, 5, 38]
another_merge_sort(array, 0, len(array) - 1)
print(array)