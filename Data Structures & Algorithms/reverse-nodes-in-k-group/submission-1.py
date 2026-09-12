# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        while n//k>=1:
            group_start = curr
            ptr = None
            count = 0
            while count < k:
                temp = curr.next
                curr.next = ptr
                ptr = curr
                curr = temp
                count+=1
            # connect previous group to reversed group
            prev.next = ptr
            # connect end of reversed group to next section
            group_start.next = curr
            # move prev to end of current reversed group
            prev = group_start
            n-=k
        
        return dummy.next