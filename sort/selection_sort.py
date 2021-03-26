# 选择排序 SelectionSort
# 原地排序算法
# 不稳定排序算法
# 时间复杂度：
# 最好、最坏、平均 O(n^2)

def find_smallest(arr, start_index, end_index):
    smallest = arr[start_index]
    smallest_index = start_index
    for i in range(start_index, end_index):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 选择排序
def selection_sort(arr):
    if len(arr) <= 1: 
        return arr

    for i in range(len(arr) - 1):
        smallest_index = find_smallest(arr, i, len(arr))
        if smallest_index != i:
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp

    return arr


def __main__():
    print(selection_sort([0, 19, 19, 48, 1, 5, 38]))


__main__()
