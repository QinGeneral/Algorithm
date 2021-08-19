/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(-1);
        ListNode newHead = result;
        while (l1 != null || l2 != null) {
            int a = l1 == null ? Integer.MAX_VALUE : l1.val;
            int b = l2 == null ? Integer.MAX_VALUE : l2.val;
            if (a < b) {
                result.next = l1;
                l1 = l1.next;
            } else {
                result.next = l2;
                l2 = l2.next;
            }
            result = result.next;
        }
        return newHead.next;
    }
}