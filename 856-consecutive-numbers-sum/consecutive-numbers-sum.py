class Solution:
    import math
    def consecutiveNumbersSum(self, n: int) -> int:
    
        count = 0
        k = 1
        # for i in range(1, int(math.sqrt(2*n))):
        while k * (k-1) // 2 < n:
            # if isinstance(n//i + i//2 + 0.5, int):
            p = n - k * (k-1)//2
            if p > 0 and (p % k == 0):
               count += 1
               print(f'count : {count}')
            k += 1
       
        return count 
            