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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode head2 = cutList(head);
        return mergeTwoList(sortList(head), sortList(head2));
    }

    public ListNode mergeTwoList(ListNode node1, ListNode node2) {
        if (node1 == null) {
            return node2;
        }
        if (node2 == null) {
            return node1;
        }
        ListNode newHead = new ListNode(-1), tail = newHead;
        while (node1 != null && node2 != null) {
            if (node1.val > node2.val) {
                tail.next = node2;
                node2 = node2.next;
            } else {
                tail.next = node1;
                node1 = node1.next;
            }
            tail = tail.next;
        }
        if (node1 != null) {
            tail.next = node1;
        } else {
            tail.next = node2;
        }
        return newHead.next;
    }

    public ListNode cutList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode fast = head, slow = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        return slow;
    }
}