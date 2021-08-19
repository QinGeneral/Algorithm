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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode tail = new ListNode(-1);
        ListNode newHead = head;
        while (newHead != null) {
            ListNode temp = newHead;
            newHead = newHead.next;

            temp.next = tail;
            tail = temp;
        }
        head.next = null;
        return tail;
    }
}