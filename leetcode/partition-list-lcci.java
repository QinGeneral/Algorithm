/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode smallerHead = new ListNode(-1);
        ListNode smallerTail = smallerHead;
        ListNode largerHead = new ListNode(-1);
        ListNode largerTail = largerHead;
        while(head != null) {
            ListNode temp = head;
            head = head.next;
            temp.next = null;
            if(temp.val < x) {
                smallerTail.next = temp;
                smallerTail = smallerTail.next;
            } else {
                largerTail.next = temp;
                largerTail = largerTail.next;
            }
        }
        smallerTail.next = largerHead.next;
        return smallerHead.next;
    }
}