/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        int i = 1;
        ListNode preHead = head;
        while (i < k && preHead != null) {
            i++;
            preHead = preHead.next;
        }
        ListNode resultNode = head;
        while (preHead != null && preHead.next != null) {
            resultNode = resultNode.next;
            preHead = preHead.next;
        }
        return resultNode;
    }
}