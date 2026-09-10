# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head # slow is the last node of the first half, with the first half always being longer or equal length of the second half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse second linked list with head slow
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # make connections
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
        