# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head.next
        merged_head = ListNode()
        merged = merged_head
        prev_merged = None

        while current_head != None:
            if current_head.val == 0:
                merged.next = ListNode()
                prev_merged = merged
                merged = merged.next
            else:
                merged.val += current_head.val
            current_head = current_head.next
        prev_merged.next = None
        return merged_head
            

