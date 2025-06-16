class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[len(strs)-1]
        a, b = len(first), len(last)
        if a < b:
            mini = a
        else:
            mini = b
        k = mini
        for i in range(mini):
            if first[i] != last[i]:
                k = i
                break
        
        return strs[0][:k]   
