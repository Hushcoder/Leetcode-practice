class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # M1 ===> using re
        # import re

        # # Using RE for matching

        # n = re.search(needle, haystack)

        # return n.start() if n else -1

        # M2 
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        
        for k in range(h):
            if haystack[k:k+n] == needle:
                return k
        return -1

        