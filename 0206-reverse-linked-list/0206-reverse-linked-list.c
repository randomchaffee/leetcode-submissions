// Aug 11, 2026 10:51
// three pointer approach

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    // edge case
    if (head == NULL) {
        return NULL;
    }

    // we set three pointers
    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    struct ListNode * next = NULL;

    // now we reverse the linked list in place
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    head = prev;

    return head;
}