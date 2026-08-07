# August 07, 2026 17:42
# we use a simple hashmap approach (not the best time complexity)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we will use a set to store the node references we find
        # we can't use the values as reference since there might be duplicates
        listed = set()

        # this will serve as our pointer
        curr = head

        # we traverse the linkedlist
        while curr is not None:
            # if the node is already in the set, we return true
            # since that means it is a cycle
            if curr in listed:
                return True
            
            # if not, then we simply add it to the map
            listed.add(curr)
            curr = curr.next
        
        # if we reach the end of the linkedlist, return False
        return False
            