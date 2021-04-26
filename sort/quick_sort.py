# quick sort
def better_quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]

    i = start
    for j in range(start, end):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    temp = arr[end]
    arr[end] = arr[i]
    arr[i] = temp
    print(arr)
    better_quick_sort(arr, start, i - 1)
    better_quick_sort(arr, i + 1, end)


def anathor_quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]

    i = start
    j = end
    isFromEnd = True
    while i < j:
        print(i, j)
        if isFromEnd:
            if arr[j] < pivot:
                arr[i] = arr[j]
                i += 1
                isFromEnd = False
            else:
                j -= 1
        else:
            if arr[i] > pivot:
                arr[j] = arr[i]
                j -= 1
                isFromEnd = True
            else:
                i += 1

    arr[i] = pivot
    print(arr)
    anathor_quick_sort(arr, start, i - 1)
    anathor_quick_sort(arr, i + 1, end)


def quick_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return arr

    pivot = arr[0]

    # complex code
    # left = []
    # right = []
    # for item in arr[1:]:
    #     if item <= pivot:
    #         left.append(item)
    #     else:
    #         right.append(item)
    # simple code
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


result = -1


def getK(arr, k, start, end):
    global result
    if start >= end:
        result = start
        return

    pivot = arr[end]

    i = start
    for j in range(start, end):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    temp = arr[end]
    arr[end] = arr[i]
    arr[i] = temp

    if i == k - 1:
        result = i
    elif i > k - 1:
        getK(arr, k, start, i - 1)
    else:
        getK(arr, k, i + 1, end)


array1 = [8, 3, 10, 2, 7, 6, 9, 12]
array2 = [5, 2, 3, 1]
# print(quick_sort([3, 2, 5, 1, 4]))
# print(quick_sort([5, 2, 3, 1]))

# better_quick_sort(array1, 0, len(array1) - 1)
print(array1)
anathor_quick_sort(array1, 0, len(array1) - 1)
# better_quick_sort(array2, 0, 3)
# print(array1, array2)

# print(getK(array1, 5, 0, 4), result, array1[result])
# print(getK(array2, 4, 0, 3), result, array2[result])