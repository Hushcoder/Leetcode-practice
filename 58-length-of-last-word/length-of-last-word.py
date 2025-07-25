class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        new_s = []
        for en in s.split(' '):
            if en != '':
                new_s.append(en)
        
        return len(new_s[-1])
