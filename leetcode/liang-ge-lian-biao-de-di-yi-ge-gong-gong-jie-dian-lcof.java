/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        int lengthA = getListLength(headA);
        int lengthB = getListLength(headB);
        ListNode longList = lengthA > lengthB ? headA : headB;
        ListNode shortList = lengthA > lengthB ? headB : headA;
        for (int i = 0; i < Math.abs(lengthA - lengthB); i++) {
            longList = longList.next;
        }
        while (longList != null) {
            if (longList == shortList) {
                return longList;
            }
            longList = longList.next;
            shortList = shortList.next;
        }
        return null;
    }

    public int getListLength(ListNode node) {
        int length = 0;
        while (node != null) {
            length++;
            node = node.next;
        }
        return length;
    }
}