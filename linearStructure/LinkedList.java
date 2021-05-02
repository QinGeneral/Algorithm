package linearStructure;

class LinkedList {

    int value = -1;
    LinkedList next = null;
    LinkedList prev = null;

    LinkedList(int value) {
        this.value = value;
    }

    LinkedList insert(LinkedList head, int value) {
        LinkedList node = new LinkedList(value);
        if (head == null) {
            head = node;
            return head;
        }
        LinkedList tail = head;
        while (tail.next != null) {
            tail = tail.next;
        }
        tail.next = node;
        node.prev = tail;
        return node;
    }

    LinkedList update(LinkedList head, int value) {
        LinkedList temp = head;
        while (temp != null) {
            if (temp.value == value) {
                return temp;
            } else {
                temp = temp.next;
            }
        }
        print(value + " not found");
        return null;
    }

    LinkedList remove(LinkedList head, int value) {
        LinkedList temp = head;
        while (temp != null) {
            if (temp.value == value) {
                if (temp == head) {
                    if (head.next != null) {
                        head.next.prev = null;
                    }
                    head = head.next;
                } else {
                    temp.prev.next = temp.next;
                }
                break;
            } else {
                temp = temp.next;
            }
        }
        return head;
    }

    public String toString(LinkedList head) {
        String result = "";
        LinkedList temp = head;
        while (temp != null) {
            result += temp.value + " ";
            temp = temp.next;
        }
        return result;
    }

    void print(String msg) {
        System.out.print(msg + "\n");
    }

    LinkedList reverse(LinkedList head) {
        LinkedList temp = head;
        LinkedList preNode = null;
        while (temp != null) {
            LinkedList tempNext = temp.next;
            temp.next = preNode;
            preNode = temp;
            temp = tempNext;
        }
        return preNode;
    }

    public static void main(String[] args) {
        LinkedList head = new LinkedList(8);
        head.insert(head, 10);
        head.print(head.toString(head));
        head.insert(head, 11);
        head.print(head.toString(head));
        head.insert(head, 9);
        head.insert(head, 7);
        head.insert(head, 3);
        head.insert(head, 4);
        head.insert(head, 6);
        head.print(head.toString(head));
        head = head.remove(head, 3);
        head = head.remove(head, 9);
        head.print(head.toString(head));
        head = head.remove(head, 8);
        head.print(head.toString(head));
        head = head.reverse(head);
        head.print(head.toString(head));
    }
}