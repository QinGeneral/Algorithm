/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode pre = null;
        ListNode h = head;
        int i = 1;
        while (h != null && i != left) {
            pre = h;
            h = h.next;
            i++;
        }
        if (h == null) {
            return head;
        }
        ListNode reverseNode = reverse(h, right - left + 1);
        if (pre == null) {
            return reverseNode;
        }
        pre.next = reverseNode;
        return head;
    }

    public ListNode reverse(ListNode head, int stop) {
        if (stop == 1) {
            return head;
        }
        ListNode pre = null, cur = head;
        int i = 1;
        while (cur != null && i != stop) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
            i++;
        }
        head.next = cur.next;
        cur.next = pre;
        return cur;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode leftPreNode = dummy;
        for (int i = 1; i < left; i++) {
            leftPreNode = leftPreNode.next;
        }
        ListNode rightNode = leftPreNode;
        for (int i = 0; i < right - left + 1; i++) {
            rightNode = rightNode.next;
        }
        ListNode leftNode = leftPreNode.next;
        leftPreNode.next = null;
        ListNode rightAfterNode = rightNode.next;
        rightNode.next = null;

        ListNode midNode =reverse(leftNode);
        leftPreNode.next = midNode;

        leftNode.next = rightAfterNode;

        return dummy.next;
    }

    public ListNode reverse(ListNode head) {
        ListNode pre = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
}