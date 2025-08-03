class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        ## With Stack
        
        stac = []
        res = ""
        for ch in s:
            if ch == "(":
                if stac: ## or (len(stac) == 0)
                    res += ch
                stac.append(ch)
            else:
                stac.pop()
                if stac:
                    res += ch
        
        return res
