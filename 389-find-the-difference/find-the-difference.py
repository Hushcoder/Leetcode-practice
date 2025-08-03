class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sums, sumt = 0,0

        for i in range(len(s)):
            sums += ord(s[i])
        
        for i in range(len(t)):
            sumt += ord(t[i])
        
        diff = sumt - sums

        return chr(diff)
