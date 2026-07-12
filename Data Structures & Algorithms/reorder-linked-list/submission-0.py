# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        # avoid cycle when list has an odd number of nodes, both first and second have the same last node --> point to itself --> cycle
        cur = slow.next
        slow.next = None # avoid when second only has one node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        second = prev
        first = head

        dummy = ListNode()
        cur = dummy
        while second and first:
            cur.next = first
            cur = cur.next
            first = first.next
            cur.next = second
            cur = cur.next
            second = second.next

        cur.next = first
        head = dummy.next