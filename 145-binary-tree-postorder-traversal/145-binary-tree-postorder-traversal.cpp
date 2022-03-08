/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ints;
        solve(root,ints);
        return ints;
        
    }
    
    void solve(TreeNode * root, vector<int> & ints) {
        if (root == nullptr) {
            return;
        }
        
        solve(root->left,ints);
        solve(root->right,ints);
        ints.push_back(root->val);
    }
};