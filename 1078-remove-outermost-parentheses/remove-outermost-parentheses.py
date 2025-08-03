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


        ### With Count
        # count = 0
        # res = ""
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         count += 1
        #     if count != 0:
        #         res += s[i]
        #     if s[i] == ")":
        #         count -= 1
        
        # return res
        
    #    2nd one Wrong Code 


