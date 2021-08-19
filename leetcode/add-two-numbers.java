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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(-1);
        ListNode cur = result;
        boolean isInc = false;
        while (l1 != null || l2 != null) {
            int n1 = l1 != null ? l1.val : 0;
            int n2 = l2 != null ? l2.val : 0;
            int n = n1 + n2;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
            if (isInc) {
                n += 1;
                isInc = false;
            }
            isInc = n > 9;
            if (isInc) {
                n = n - 10;
            }
            ListNode temp = new ListNode(n);
            cur.next = temp;
            cur = temp;
        }
        if (isInc) {
             ListNode temp = new ListNode(1);
            cur.next = temp;
        }
        return result.next;
    }
}