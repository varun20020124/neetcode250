# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val,i,node)) # (val,Node)
        curr = dummy
        while heap:
            val,idx,node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val,idx, node.next))
        return dummy.next