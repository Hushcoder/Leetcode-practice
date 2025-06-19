class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31 , 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        while x > 0:
            rem = x % 10
            ans = rem + ans * 10
            x = x // 10
        
        ans *= sign

        if ans < int_min or ans > int_max:
            return 0
        return ans