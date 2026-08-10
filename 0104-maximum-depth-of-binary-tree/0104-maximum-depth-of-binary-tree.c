/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


// helper function for getting the max value of two ints
int getMaximum(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}

// helper function for the postorder DFS traversal
int dfs(struct TreeNode* node) {
    if (node == NULL) {
        return 0;
    }

    return 1 + getMaximum(dfs(node->left), dfs(node->right));
}

int maxDepth(struct TreeNode* root) {
    struct TreeNode *node_ptr = root;

    return dfs(root);
}