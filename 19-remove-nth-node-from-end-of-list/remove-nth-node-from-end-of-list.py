# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, head: Optional[ListNode]) -> int :
        if head is None :
            return 0
        curr = head
        length = 0
        while curr != None :
            length += 1
            curr = curr.next
        return length
                     
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.len(head)
        if l <= 1 :
            return None
        if l == n :
            return head.next
        curr = head
        for _ in range(l-n-1):
            curr = curr.next
        if curr.next is None:
            curr = head
            curr.next = None
        else : 
            temp = curr.next
            curr.next = temp.next
            temp.next = None

        return head

        
        