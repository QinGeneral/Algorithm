let MaxHeap = {
    init: function () {
        this.array = [0];
    },
    buildByInsert: function (array) {
        this.init();
        for (let i = 0; i < array.length; i++) {
            this.insert(array[i]);
        }
    },
    buildByLinear: function (array) {
        this.array = array;
        for (let i = parseInt((array.length - 1) / 2); i > 0; i--) {
            this.moveDown(i, this.array.length);
        }
    },
    pop: function () {
        let firstI = 1;
        let value = this.array[firstI];
        this.array[firstI] = this.array[this.array.length - 1];
        this.moveDown(firstI, this.array.length);
        this.array.pop();
        return value;
    },
    moveDown: function (i, n) {
        while (true) {
            let targetI = i;
            if (i * 2 < n && this.array[targetI] < this.array[i * 2]) {
                targetI = i * 2;
            }
            if (i * 2 + 1 < n && this.array[targetI] < this.array[i * 2 + 1]) {
                targetI = i * 2 + 1;
            }
            if (targetI == i) {
                break;
            }
            this.swap(this.array, i, targetI);
            i = targetI;
        }
    },
    insert: function (value) {
        this.array.push(value);

        let i = this.array.length - 1;
        this.moveUp(i);
    },
    moveUp: function (i) {
        while (true) {
            let parentI = parseInt(i / 2);
            if (parentI > 0 && this.array[parentI] < this.array[i]) {
                this.swap(this.array, i, parentI);
                i = parentI;
                parentI = parseInt(i / 2);
            } else {
                break;
            }
        }
    },
    swap: function (array, i, j) {
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    },
    sort: function () {
        let i = this.array.length - 1;
        while (i > 1) {
            let firstI = 1;
            this.swap(this.array, firstI, i);
            this.moveDown(firstI, i);
            i--;
        }
    }
};

let heap = MaxHeap;
heap.init();
heap.insert(5);
heap.insert(3);
heap.insert(6);
heap.insert(9);
heap.insert(1);
heap.insert(10);
console.log(heap.array);

heap.buildByInsert([1, 3, 2, 9, 5, 4, 11, 7]);
console.log(heap.array);

heap.buildByLinear([0, 1, 3, 2, 9, 5, 4, 11, 7]);
console.log(heap.array);

console.log(heap.pop());
console.log(heap.array);

heap.sort();
console.log(heap.array);