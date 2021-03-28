function InsertSort(array) {
    if (array.length <= 1) {
        return array;
    }
    for (var i = 1; i < array.length; i++) {
        var temp = array[i];
        var j = i - 1;
        while (j >= 0) {
            if (temp < array[j]) {
                array[j + 1] = array[j];
            }
            else {
                break;
            }
            j--;
            array[j + 1] = temp;
        }
    }
    return array;
}
console.log(InsertSort([4, 5, 6, 1, 3, 2, 1, 3, 5, 23, 134, 45, 1, 4, 5]));
