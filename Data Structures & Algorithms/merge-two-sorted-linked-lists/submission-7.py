# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()

        curr = dummyNode
        temp1 = l1
        temp2 = l2

        while temp1 and temp2:
            if temp1.val < temp2.val:
                curr.next = temp1
                temp1 = temp1.next
                
            else:
                curr.next = temp2
                temp2 = temp2.next
            
            curr = curr.next

        if temp2:
            curr.next = temp2
        if temp1:
            curr.next = temp1

        return dummyNode.next




        