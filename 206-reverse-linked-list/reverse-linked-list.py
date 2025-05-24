# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        if head is None :
            return None 
        while current != None :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def actual_reverse(self, head: Optional[ListNode]) -> List[int]:
        r = self.reverseList(head)
        if r is None :
            return []
        res = []
        current = r
        while current != None :
            res.append(current.key)
            current = current.next
        return res
            


