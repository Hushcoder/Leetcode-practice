class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n == 1:
            return True
        if n%2 != 0 or n <= 0:
            return False
        
        x = math.log2(n)
        if x.is_integer():
            return True
        else:
            return False
        