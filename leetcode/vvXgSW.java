import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        ListNode head = new ListNode(-1);
        ListNode tail = head;
        while (true) {
            int min = Integer.MAX_VALUE;
            int minI = -1;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] != null && lists[i].val < min) {
                    min = lists[i].val;
                    minI = i;
                }
            }
            if (minI == -1) {
                break;
            } else {
                tail.next = lists[minI];
                tail = tail.next;
                lists[minI] = lists[minI].next;
            }
        }
        return head.next;
    }
}

class Solution2 {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        ListNode head = new ListNode(-1);
        ListNode tail = head;
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(new Comparator<ListNode>(){

            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val > o2.val ? 1 : -1;
            }
            
        });
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                minHeap.add(lists[i]);
            }
        }
        while(minHeap.size() > 0) {
            ListNode temp = minHeap.poll();
            if (temp.next != null) {
                minHeap.add(temp.next);
            }
            tail.next = temp;
            tail = tail.next;
        }
        return head.next;
    }
}