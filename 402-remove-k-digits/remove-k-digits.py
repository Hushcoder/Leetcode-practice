class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stac = []
        res = ""
        for ch in num:
            while(k>0 and len(stac)>0) and (stac[-1]>ch):
                stac.pop(len(stac) - 1)
                k -= 1
            stac.append(ch)
        
        while(k>0 and len(stac)>0):
            stac.pop(len(stac)-1)
            k -= 1
        
        while(len(stac)>0 and stac[0] == "0"):
            stac.pop(0)

        return "0" if len(stac) == 0 else res.join(stac)