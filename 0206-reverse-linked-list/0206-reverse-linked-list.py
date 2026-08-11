# Aug 11, 2026 10:47
# three pointer approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if head is None:
            return None
        
        # we set three pointers
        # prev will point to the previous node, initially null
        # curr will initially point to the head
        # next will point to the next node so we can keep track of the linked list
        prev = None
        curr = head
        next = None

        # now we modify the connections of the nodes in place
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev
        
        return head
