# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #My Code :- Correct but gives TLE 
        # if pos == -1:
        #     return False
        # length = 0
        # temp = head
        # while temp:
        #     length += 1
        #     temp = temp.next
            
        # visited = []
        # curr = head
        # i = 0 
        # while curr.next != None:
        #     if curr in visited:
        #         break
        #     visited.insert(i, curr)
        #     curr = curr.next
        #     i += 1
        
        # if curr.next == visited[pos]:
        #     return True
        # else:
        #     return False
        
        
        # Optimized Code :- Tortoise & Hare Algorithm (Floyd Method)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
              
