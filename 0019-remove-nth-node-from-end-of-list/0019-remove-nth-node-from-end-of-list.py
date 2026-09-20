# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        prev = None

        # get the length of the linked list
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        
        # set the length to the nth node
        length -= n - 1

        # reset curr
        curr = head

        # go to the nth node
        for i in range(0, length - 1):
            prev = curr
            curr = curr.next
        
        # n is at the head
        if curr == head:
            head = head.next
            return head

        prev.next = curr.next
        return head
