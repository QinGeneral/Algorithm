function quickSort(array: number[], start: number, end: number) {
    if (start >= end) {
        return;
    }
    let pivot = array[end];

    let i = start;
    for (let j = start; j < end; j++) {
        if (array[j] < pivot) {
            let temp = array[j];
            array[j] = array[i];
            array[i] = temp;
            i++;
        }
    }
    let temp = array[end];
    array[end] = array[i];
    array[i] = temp;

    quickSort(array, start, i - 1);
    quickSort(array, i + 1, end);
}