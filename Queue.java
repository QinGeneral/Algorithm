public class Queue {
    
    String[] array;
    int head;
    int tail;
    int count;

    Queue(int count) {
        array = new String[count];
        this.count = count;
        head = 0;
        tail = 0;
    }

    boolean enqueue(String item) {
        if (tail == count) {
            if (head == 0)
                return false;
            else {
                for (int i = head; i < tail; i++) {
                    array[i - head] = array[i];
                }
                tail = tail - head;
                head = 0;
            }
        }
        array[tail] = item;
        tail++;
        return true;
    }

    String dequeue() {
        if (head == tail) {
            return null;
        }
        String result = array[head];
        head++;
        return result;
    }
}