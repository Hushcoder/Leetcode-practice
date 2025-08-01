class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = sorted(set(nums), reverse=True) # O(nlogn)
        
        return nums[2] if len(nums) >= 3 else nums[0]


 

        # print(sorted(set(nums), reverse=True))