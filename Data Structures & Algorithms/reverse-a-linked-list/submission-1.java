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
        ListNode prev = null;
        ListNode cursor = head;

        while (cursor != null) {
            ListNode next = cursor.next;
            cursor.next = prev;
            prev = cursor;
            cursor = next;
        }
        return prev;
    }
}
