# 冒泡排序 Bubble Sort
# 原地排序算法
# 稳定排序算法
# 时间复杂度：
# 最好 O(n)、最坏 O(n^2)、平均 O(n^2)

def bubble_sort(array):
    if len(array) <= 1:
        return array

    print(array)
    for i in range(len(array), 0, -1):
        print("begin", i)
        is_not_change = True
        for j in range(1, i):
            if array[j] < array[j - 1]:
                is_not_change = False
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
        print(i, array, is_not_change)
        if is_not_change:
            break
    return array

print(bubble_sort([4, 5, 6, 3, 2, 1]))
print(bubble_sort([3, 5, 4, 1, 2, 6]))