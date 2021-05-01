function mergeSort(array: number[], start: number, end: number) {
    if (start >= end) {
        return;
    }
    let mid = Math.floor((start + end) / 2);

    mergeSort(array, start, mid);
    mergeSort(array, mid + 1, end);

    let i = start;
    let j = mid + 1;

    let tmpArray = [];
    while (i <= mid && j <= end) {
        if (array[i] < array[j]) {
            tmpArray.push(array[i++]);
        } else {
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
    for (let i = start; i <= end; i++) {
        array[i] = tmpArray[i - start];
    }
}

let array = [0, 19, 19, 48, 1, 5, 38]
mergeSort(array, 0, array.length - 1)
console.log(array);
