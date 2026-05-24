# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        heap = []

        for i,node in enumerate(lists):

            if node == None:
                pass
            else:

                tup = (node.val,i,node)

                heapq.heappush(heap,tup)

        res = ListNode(0)
        point = res
        while heap:
            
            smallest = heapq.heappop(heap)
            val, index, node = smallest

            point.next = node
            point = point.next

            if node.next is None:
                pass
            else:
                heapq.heappush(heap, (node.next.val,index,node.next))


        return res.next




            

    



    