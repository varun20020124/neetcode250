# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse linked list
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        ptr = None
        curr = prev
        for _ in range(n-1):
            ptr = curr
            curr = curr.next
        if ptr is None:
            # removing head of reversed list
            prev = curr.next
        else:
            ptr.next = curr.next
        # reverse again
        curr = prev
        ptr2 = None
        while curr:
            temp = curr.next
            curr.next = ptr2
            ptr2 = curr
            curr = temp
        return ptr2