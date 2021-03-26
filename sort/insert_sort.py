# 插入排序
# 原地排序算法
# 稳定排序算法
# 时间复杂度：
# 最好 O(n)、最坏 O(n^2)、平均 O(n^2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

def better_insert_sort(array):
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0:
            if temp < array[j]:
                array[j + 1] = array[j]
            else:
                break
            j -= 1
        array[j + 1] = temp
    return array


def insert_sort(array):
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] < array[j]:
                temp = array[i]
                for k in range(i - 1, j - 1, -1):
                    array[k + 1] = array[k]
                array[j] = temp
                break
    return array


print(better_insert_sort([4, 5, 6, 1, 3, 2, 1, 3, 5, 23, 134, 45, 1, 4, 5]))
print(insert_sort([4, 5, 6, 1, 3, 2, 1, 3, 5, 23, 134, 45, 1, 4, 5]))
print(list(range(0, 1)), list(range(5, 1, -1)))
