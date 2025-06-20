class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s)
        new_str_lower = ''
        for char in new_str:
            if char.isupper():
                new_str_lower += char.lower()
            else:
                new_str_lower += char

        rev_str = ''
        for i in range(len(new_str_lower)-1,-1,-1):
            rev_str += new_str_lower[i]
        
        return True if rev_str == new_str_lower else False




               