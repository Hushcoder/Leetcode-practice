class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # nums = sorted(set(nums), reverse=True) # O(nlogn)
        
        # return nums[2] if len(nums) >= 3 else nums[0]

        ## In => O(n) TC

        mx1 = mx2 = mx3 = float('-inf')

        for num in nums:
            if num == mx1 or num == mx2 or num == mx3:
                continue
            elif num > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = num
            elif num > mx2:
                mx3 = mx2
                mx2 = num
            elif num > mx3:
                mx3 = num
        
        if mx3 == float('-inf'):
            return mx1
        else:
            return mx3


 

        # print(sorted(set(nums), reverse=True))