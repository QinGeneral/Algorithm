public class QueueCycle {
    
    String[] array;
    int head;
    int tail;
    int count;

    QueueCycle(int count) {
        array = new String[count];
        this.count = count;
        head = 0;
        tail = 0;
    }

    boolean enqueue(String item) {
        if ((tail + 1) % count == head) {
            return false;
        }
        array[tail] = item;
        tail = (tail + 1) % count;
        return true;
    }

    String dequeue() {
        if (head == tail) {
            return null;
        }
        String result = array[head];
        head = (head + 1) % count;
        return result;
    }
}