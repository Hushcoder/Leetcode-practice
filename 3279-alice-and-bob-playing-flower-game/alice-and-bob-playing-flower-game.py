class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        if n == 1 and m == 1:
           return 0
        
        oddx = (n + 1) // 2
        evenx = n // 2

        oddy = (m + 1) // 2
        eveny = m // 2

        ans = (oddx * eveny) + (evenx * oddy)

        return ans
        