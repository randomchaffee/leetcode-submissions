# August 03, 2026 01:30

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first we create a dummy node
        newHead = ListNode(-1)
        # we create a pointer to keep track of the dummy node
        curr = newHead
        # since we already have list1 and list2,


        # we iterate through both linked lists until
        # we reach their tails
        while list1 is not None and list2 is not None:
            # if the value of the list1 is lower than list2
            # we connect it to the new linked list
            # and set the head of list1 to the next node
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            # vice versa if list2 is lower than list1
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        # append any remaining nodes to our linked list
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2
        
        return newHead.next
