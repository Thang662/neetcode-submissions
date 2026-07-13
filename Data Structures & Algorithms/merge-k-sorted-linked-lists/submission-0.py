# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    tail = tail.next
                    l1 = l1.next
                else:
                    tail.next = l2
                    tail = tail.next
                    l2 = l2.next
            tail.next = l1 if l1 else l2
            return dummy.next

        while len(lists) > 1:
            merge_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merge_list.append(merge_two(l1, l2))
            lists = merge_list
        return lists[0]
