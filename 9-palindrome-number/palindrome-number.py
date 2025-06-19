class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_str = ""
        for i in range(len(str_x)-1,-1,-1):
            rev_str += str_x[i]
        
        return True if rev_str == str_x else False