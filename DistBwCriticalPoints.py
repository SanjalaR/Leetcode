# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        cp = []
        prev = head
        curr = head.next
        pos = 1
        while curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                cp.append(pos)
            prev = curr
            curr = curr.next
            pos+=1
        
        if len(cp)<2:
            return [-1, -1]

        min_d = float('inf')
        max_d = cp[-1] - cp[0]

        for i in range(1, len(cp)):
            min_d = min(min_d, cp[i]-cp[i-1])

        return [min_d, max_d]
        
