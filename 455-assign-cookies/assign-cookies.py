class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # sort 
        g.sort()
        s.sort()

        l = r = 0

        n,m = len(g), len(s)

        # logic loop
        while (l < n and r < m):
            if g[l] <= s[r]:
                l += 1
            r += 1

        return l