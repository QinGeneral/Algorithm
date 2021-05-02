package linearStructure;
class Stack {

    String[] array;
    int count;
    int head = 0;

    Stack(int count) {
        array = new String[count];
        this.count = count;
    }

    boolean push(String i) {
        if (head == count) {
            return false;
        }
        array[head] = i;
        head++;
        return true;
    }

    String pop() {
        head--;
        if (head < 0) {
            head = 0;
            return null;
        }
        String result = array[head];
        return result;
    }
}