# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # adding node 0 at head of list
        tracker = head
        remover = dummy

        while n > 0:
            tracker = tracker.next
            n -= 1
        
        while tracker:
            tracker = tracker.next
            remover = remover.next
        
        remover.next = remover.next.next
        return dummy.next
        