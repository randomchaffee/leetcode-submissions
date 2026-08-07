/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    // we create two pointers 'slow' and 'fast'
    // which we use to determine if the linked has a cycle
    struct ListNode *slow = head; // 1 step
    struct ListNode *fast = head; // 2 steps

    // now we try to find a cycle
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        // if slow and fast reach the same node 
        // that means we have a cycle!
        if (slow == fast) {
            return true;
        }
    }
    return false;
}
