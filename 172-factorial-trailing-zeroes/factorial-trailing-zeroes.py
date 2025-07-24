class Solution:
    def trailingZeroes(self, n: int) -> int:
        
          ###### Recursion solution ---> depth of rec. tree inc. for large input . TC -> O(n) , SC -> O(n)
    #     factorial = self.factNum(n)
        
    #     ## count for trailing zeroes
    #     count = 0
    #     while factorial > 0:
    #         mod = factorial % 10
    #         if mod == 0:
    #             count += 1
    #             print(f'count : {count}')
    #         else:
    #             break
    #         factorial //= 10
        
    #     return count

    # ## factNum for factorial
    # def factNum(self, n: int) -> int:

    #     if n == 0 or n == 1:
    #         return 1
        
    #     return n * self.factNum(n-1)


    ### Mathematical Insight , TC -> O(logn) , SC -> O(1)

        count = 0

        while n >= 5:
            n //= 5
            count += n
        return count