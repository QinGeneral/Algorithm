class LRUCache {

    int capacity = 5;
    int count = 0;
    Node head = new Node(0, 0);
    Node tail = head;

    class Node {
        int key;
        int value;
        Node next;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        Node temp = head.next;
        Node pre = head;
        while (temp != null) {
            if (temp.key == key) {
                pre.next = temp.next;
                while (pre.next != null) {
                    pre = pre.next;
                }
                pre.next = temp;
                temp.next = null;
                print();
                return temp.value;
            }
            pre = temp;
            temp = temp.next;
        }
        print();
        return -1;
    }
    
    public void put(int key, int value) {
        Node temp = head.next;
        Node pre = head;
        while (temp != null) {
            if (temp.key == key) {
                pre.next = temp.next;
                while (pre.next != null) {
                    pre = pre.next;
                }
                pre.next = temp;
                temp.next = null;
                temp.value = value;
                print();
                return;
            }
            pre = temp;
            temp = temp.next;
        }

        if (this.count == this.capacity) {
            Node next = this.head.next;
            head.next = next.next;
            this.count--;
            if (next.key == pre.key) {
                pre = head;
            }
        }
        Node node = new Node(key, value);
        pre.next = node;
        this.count++;
        print();
    }

    public void print() {
        // Node temp = head.next;
        // while (temp != null) {
        //     System.out.print(temp.key + " " + temp.value + "; ");
        //     temp = temp.next;
        // }
        // System.out.println();
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

class LRUCache {

    int capacity = 5;
    int count = 0;
    Node head = new Node(0, 0);
    Node tail = new Node(0, 0);
    HashMap<Integer, Node> map = new HashMap<>();

    class Node {
        int key;
        int value;
        Node next;
        Node prev;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head.next = this.tail;
        this.head.prev = this.tail;
        this.tail.next = this.head;
        this.tail.prev = this.head;
    }
    
    public int get(int key) {
        Node node = this.map.get(key);
        if (node == null) {
            return -1;
        }
        moveToLast(node);
        print();
        return node.value;
    }

    public void moveToLast(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;

        Node tailPrev = this.tail.prev;
        node.next = this.tail;
        node.prev = tailPrev;
        this.tail.prev = node;
        tailPrev.next = node;
    }
    
    public void put(int key, int value) {
        Node node = this.map.get(key);
        if (node != null) {
            node.value = value;
            moveToLast(node);
            return;
        }
        if (this.map.size() == this.capacity) {
            Node next = this.head.next;
            this.head.next = next.next;
            next.next.prev = this.head;
            next.prev = null;
            next.next = null;
            this.map.remove(next.key);
        }
        node = new Node(key, value);
        Node tailPrev = this.tail.prev;
        node.next = this.tail;
        node.prev = tailPrev;
        this.tail.prev = node;
        tailPrev.next = node;

        this.map.put(key, node);
        print();
    }

    public void print() {
        // Node temp = this.head.next;
        // while (temp != this.tail) {
        //     System.out.print(temp.key + " " + temp.value + "; ");
        //     temp = temp.next;
        // }
        // System.out.println();
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */