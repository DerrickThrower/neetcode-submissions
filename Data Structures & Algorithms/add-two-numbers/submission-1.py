# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        def toNum(node):
            place = 1
            num = node.val
            p1 = node.next
            while p1:

                place = place * 10
                num += p1.val * place
                p1 = p1.next

            return num

        
        val1 = toNum(l1)
        val2 = toNum(l2)

        ans = val1 + val2

        ans = reversed(list(str(ans)))
        head = ListNode(0)
        p3 = head
        for i in ans:
            p3.next = ListNode(i)

            p3 = p3.next


        return head.next

    

        


        