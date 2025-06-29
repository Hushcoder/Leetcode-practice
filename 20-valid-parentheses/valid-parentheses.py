class Solution:
    def isValid(self, s: str) -> bool:
        clo = {')':'(',']':'[','}':'{'}
        stack = []

        for c in s:
            if c in clo.values():
                stack.append(c)
            elif c in clo:
                if not stack or stack[-1] != clo[c]:
                    return False
                stack.pop()
            else:
                pass
        
        return not stack

