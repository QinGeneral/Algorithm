function mergeSort(array, start, end) {
    if (start >= end) {
        return;
    }
    var mid = Math.floor((start + end) / 2);
    mergeSort(array, start, mid);
    mergeSort(array, mid + 1, end);
    var i = start;
    var j = mid + 1;
    var tmpArray = [];
    while (i <= mid && j <= end) {
        if (array[i] < array[j]) {
            tmpArray.push(array[i++]);
        }
        else {
            tmpArray.push(array[j++]);
        }
    }
    while (i <= mid) {
        tmpArray.push(array[i++]);
    }
    while (j <= end) {
        tmpArray.push(array[j++]);
    }
    console.log(tmpArray.length, start, end);
    for (var i_1 = start; i_1 <= end; i_1++) {
        array[i_1] = tmpArray[i_1 - start];
    }
}
var array = [0, 19, 19, 48, 1, 5, 38];
mergeSort(array, 0, array.length - 1);
console.log(array);
