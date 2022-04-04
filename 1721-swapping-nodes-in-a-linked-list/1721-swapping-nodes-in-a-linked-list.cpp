/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {

        int num = 0;
        ListNode * t = head;
        int c = k;
        ListNode * h1 = head;
        while (t != nullptr) {
            t = t->next;
            num++;
            if (c > 1) {
                h1 = h1->next;
                c--;
            } else {
                
            }
        }
        ListNode * h2 = head;
        c = 0;
        while( c < (num -k)) {
            h2 = h2->next;
            c++;
        }

        int temp = h2->val;
        h2->val = h1->val;
        h1->val = temp;
        return head;
        
    }
};