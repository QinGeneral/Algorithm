package linearStructure;

class Array {

    int[] data;
    int tail = -1;
    int length;

    Array() {
        length = 10;
        data = new int[length];
    }

    Array(int length) {
        this.length = length;
        data = new int[length];
    }

    void expanse() {
        int[] newArray = new int[length * 2];
        for (int i = 0; i <= tail; i++) {
            newArray[i] = this.data[i];
        }
        this.data = newArray;
    }

    int insert(int value) {
        if (tail == -1) {
            data[0] = value;
            tail = 0;
            return 0;
        }
        if (tail == this.length - 1) {
            expanse();
        }
        int i = 0;
        boolean isInserted = false;
        for (; i <= tail; i++) {
            if (value < this.data[i]) {
                for (int j = tail; j >= i; j--) {
                    this.data[j + 1] = this.data[j];
                }
                this.data[i] = value;
                isInserted = true;
                break;
            }
        }
        tail++;
        if (!isInserted) {
            this.data[tail] = value;
        }
        return i;
    }

    void update(int i, int value) {
        if (i > length - 1) {
            print("插入失败");
            return;
        }
        this.data[i] = value;
    }

    void remove(int value) {
        int i = binarySearch(value);
        if (i == -1) {
            print(value + " not found");
            return;
        }
        for (int j = i; j < tail; j++) {
            this.data[j] = this.data[j + 1];
        }
        tail--;
    }

    int binarySearch(int value) {
        int low = 0;
        int high = tail;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (value == this.data[mid]) {
                return mid;
            } else if (value > this.data[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    @Override
    public String toString() {
        String result = "";
        for (int i = 0; i <= tail; i++) {
            result += this.data[i] + " ";
        }
        return result;
    }

    void print(String msg) {
        System.out.print(msg + "\n");
    }

    public static void main(String[] args) {
        Array array = new Array();
        array.insert(10);
        array.print(array.toString());
        array.insert(11);
        array.print(array.toString());
        array.insert(9);
        array.print(array.toString());
        array.remove(3);
        array.remove(9);
        array.print(array.toString());
    }
}