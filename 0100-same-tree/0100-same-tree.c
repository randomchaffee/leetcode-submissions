// Aug 9, 2026 21:12
// a simple preorder traversal approach, but in C
// I already made the same solution earlier, but in python

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// i put the helper function outside, it's a C thing
bool traverseTree(struct TreeNode* p, struct TreeNode* q) {
    // if both are null, we return true
    if (p == NULL && q == NULL) {
        return 1;
    }

    // if only one of them is NULL, we return false
    if (p == NULL || q == NULL) {
        return 0;
    }

    // value comparison
    if (p->val != q->val) {
        return 0;
    }

    // we continue recursively traversing the tree
    bool left = traverseTree(p->left, q->left);
    bool right = traverseTree(p->right, q->right);

    return left && right;
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    return traverseTree(p, q);
}