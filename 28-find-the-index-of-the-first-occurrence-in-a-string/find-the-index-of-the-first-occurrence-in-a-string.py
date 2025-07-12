class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re

        # Using RE for matching

        n = re.search(needle, haystack)

        return n.start() if n else -1