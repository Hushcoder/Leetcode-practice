# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
 
        # My Intuition 
        carry = 0
        ls = ListNode(0)
        temp = ls

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            ls.next = ListNode(total%10)
            carry = total//10
            ls = ls.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            ls.next = ListNode(carry)

        return temp.next







        
        