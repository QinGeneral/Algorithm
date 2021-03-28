// # 冒泡排序 Bubble Sort
// # 原地排序算法
// # 稳定排序算法
// # 时间复杂度：
// # 最好 O(n)、最坏 O(n^2)、平均 O(n^2)
function BubbleSort(array) {
    if (array.length <= 1) {
        return array;
    }
    for (var i = array.length - 1; i >= 0; i++) {
        var isNoChange = true;
        for (var j = 0; j < i; j++) {
            if (array[j] < array[j - 1]) {
                isNoChange = false;
                var temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
            }
        }
        if (isNoChange) {
            break;
        }
    }
    return array;
}
var array = [4, 5, 6, 3, 2, 1];
console.log(BubbleSort(array));
