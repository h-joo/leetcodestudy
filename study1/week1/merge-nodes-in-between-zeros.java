// https://leetcode.com/problems/merge-nodes-in-between-zeros/
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
    // Time Complexity: O(n)
    // Space Compexity: O(n)
    public ListNode mergeNodes(ListNode head) {
        ListNode result = new ListNode();
        ListNode iterator = result;
        int temp = 0;

        while (head != null) {
            if (head.val == 0 && temp != 0) {
                iterator.val = temp;
                temp = 0;
                if (head.next != null) {    // last ListNode
                    iterator.next = new ListNode();
                    iterator = iterator.next;
                }
            } else if (head.val != 0) {
                temp += head.val;
            }
            head = head.next;
        }

        return result;
    }
}