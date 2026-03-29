# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        s1=""
        s2=""
        dummy = ListNode(0,None)
        nnn = dummy
        while curr1:
            s1 = s1+ str(curr1.val)
            curr1 = curr1.next
        while curr2:
            s2 = s2+ str(curr2.val)
            curr2 = curr2.next
        
        v1 = int(s1[::-1])
        v2 = int(s2[::-1])

        add = v1+v2
        revadd = str(add)[::-1]
        for i in revadd:
            nnn.next = ListNode(int(i))
            nnn = nnn.next
        return dummy.next





        