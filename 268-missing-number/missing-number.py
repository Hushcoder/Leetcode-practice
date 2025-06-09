class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # My code complexity :- O[n^2]
        # a = 0
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         a = i
        #     else:
        #         pass
        # return a

        # Code :- O[n]
        n = len(nums)
        total_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return total_sum-actual_sum

