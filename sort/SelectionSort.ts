// 选择排序 SelectionSort
// 原地排序算法
// 不稳定排序算法
// 时间复杂度：
// 最好、最坏、平均 O(n^2)

function selectionSort(array: number[]) {
    if (array.length <= 1) {
        return array;
    }
    for (let i = 0; i < array.length - 1; i++) {
        let minIndex = findMin(array, i, array.length);
        if (minIndex != i) {
            let temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }
    return array;
}

function findMin(array: number[], startIndex: number, endIndex: number) {
    let min = array[startIndex];
    let minIndex = startIndex;
    for (let i = startIndex; i < endIndex; i++) {
        if (array[i] < min) {
            min = array[i];
            minIndex = i;
        }
    }
    return minIndex;
}