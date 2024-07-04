# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* mod = head->next;
        ListNode* nextSum = mod;
        while(nextSum!=nullptr){
            int sum = 0;
            while(nextSum->val!=0){
                sum+=nextSum->val;
                nextSum = nextSum->next;
            }
            mod->val = sum;
            nextSum = nextSum->next;
            mod->next = nextSum;
            mod = mod->next;
        }
        return head->next;
    }
};
