class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Takes O(N^2) Complexity
        # if s == goal:
        #     return True
        # for i in range(1,len(s)):
        #     str_part = s[:i]
        #     rest_part = s[i:]
        #     new_s = rest_part + str_part
        #     if new_s == goal:
        #         return True
        # return False

        return (len(s) == len(goal)) and (goal in (s+s))

